#!/usr/bin/env python3
"""LT-orai: naujausi faktiniai stebėjimai arba artimiausia prognozė."""
import json
import urllib.request
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

BASE = "https://api.meteo.lt/v1"
CITIES = [
    ("Vilnius", "vilniaus-ams", "vilnius"),
    ("Kaunas", "kauno-ams", "kaunas"),
    ("Klaipėda", "klaipedos-ams", "klaipeda"),
    ("Šiauliai", "siauliu-ams", "siauliai"),
    ("Panevėžys", "panevezio-ams", "panevezys"),
]
CONDITIONS = dict(zip(
    ["clear","partly-cloudy","cloudy-with-sunny-intervals","cloudy","light-rain","rain","heavy-rain","thunder","isolated-thunderstorms","thunderstorms","heavy-rain-with-thunderstorms","light-sleet","sleet","freezing-rain","hail","light-snow","snow","heavy-snow","fog"],
    ["giedra","mažai debesuota","debesuota su pragiedruliais","debesuota","nedidelis lietus","lietus","smarkus lietus","perkūnija","trumpas lietus su perkūnija","lietus su perkūnija","smarkus lietus su perkūnija","nedidelė šlapdriba","šlapdriba","lijundra","kruša","nedidelis sniegas","sniegas","smarkus sniegas","rūkas"]
))

def get(path):
    req = urllib.request.Request(BASE + path, headers={"User-Agent": "LT-orai/1.0"})
    with urllib.request.urlopen(req, timeout=15) as response:
        return json.load(response)

def utc_time(value):
    return datetime.fromisoformat(value.replace(" ", "T").replace("Z", "+00:00")).replace(tzinfo=timezone.utc) if "+" not in value and not value.endswith("Z") else datetime.fromisoformat(value.replace(" ", "T").replace("Z", "+00:00")).astimezone(timezone.utc)

def weather(station, place):
    try:
        rows = get(f"/stations/{station}/observations/latest").get("observations", [])
        valid = [x for x in rows if x.get("airTemperature") is not None and x.get("observationTimeUtc")]
        if valid:
            x = max(valid, key=lambda x: utc_time(x["observationTimeUtc"]))
            return x, utc_time(x["observationTimeUtc"]), "stebėjimas"
    except (OSError, ValueError, KeyError):
        pass
    rows = get(f"/places/{place}/forecasts/long-term").get("forecastTimestamps", [])
    now = datetime.now(timezone.utc)
    valid = [x for x in rows if x.get("airTemperature") is not None and x.get("forecastTimeUtc") and utc_time(x["forecastTimeUtc"]) >= now]
    if not valid:
        raise ValueError("Nėra artimiausios prognozės")
    x = min(valid, key=lambda x: utc_time(x["forecastTimeUtc"]))
    return x, utc_time(x["forecastTimeUtc"]), "prognozė"

def main():
    print("| Miestas | Temperatūra | Oro sąlygos | Duomenų tipas | Laikas (LT) |")
    print("|---|---:|---|---|---|")
    for name, station, place in CITIES:
        try:
            x, when, kind = weather(station, place)
            temp = f'{x["airTemperature"]:g} °C'
            condition = CONDITIONS.get(x.get("conditionCode"), "nenurodyta")
            local = when.astimezone(ZoneInfo("Europe/Vilnius")).strftime("%Y-%m-%d %H:%M")
            print(f"| {name} | {temp} | {condition} | {kind} | {local} |")
        except (OSError, ValueError, KeyError, TypeError):
            print(f"| {name} | duomenų nėra | duomenų nėra | — | — |")
    print("\nŠaltinis: Lietuvos hidrometeorologijos tarnyba (meteo.lt), https://api.meteo.lt/")
    print("Gauta:", datetime.now(ZoneInfo("Europe/Vilnius")).strftime("%Y-%m-%d %H:%M"), "(Lietuvos laiku)")

if __name__ == "__main__":
    main()
