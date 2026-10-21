#!/usr/bin/env python3
"""LT-orai: dabartinės modeliuotos oro sąlygos iš Open-Meteo."""
import json
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

CITIES = [
    ("Vilnius", 54.6872, 25.2797),
    ("Kaunas", 54.8985, 23.9036),
    ("Klaipėda", 55.7033, 21.1443),
    ("Šiauliai", 55.9349, 23.3137),
    ("Panevėžys", 55.7348, 24.3575),
]
CODES = {
    0: "giedra", 1: "daugiausia giedra", 2: "mažai debesuota",
    3: "debesuota", 45: "rūkas", 48: "šerkšno rūkas",
    51: "silpna dulksna", 53: "dulksna", 55: "stipri dulksna",
    56: "silpna lijundra", 57: "stipri lijundra",
    61: "silpnas lietus", 63: "lietus", 65: "smarkus lietus",
    66: "silpnas šąlantis lietus", 67: "stiprus šąlantis lietus",
    71: "silpnas sniegas", 73: "sniegas", 75: "smarkus sniegas",
    77: "sniego kruopos", 80: "silpnas trumpalaikis lietus",
    81: "trumpalaikis lietus", 82: "smarkus trumpalaikis lietus",
    85: "silpnas trumpalaikis sniegas", 86: "smarkus trumpalaikis sniegas",
    95: "perkūnija", 96: "perkūnija su nedidele kruša",
    99: "perkūnija su stipria kruša",
}

def fetch():
    params = {
        "latitude": ",".join(str(c[1]) for c in CITIES),
        "longitude": ",".join(str(c[2]) for c in CITIES),
        "current": "temperature_2m,weather_code",
        "timezone": "Europe/Vilnius",
        "timeformat": "unixtime",
    }
    url = "https://api.open-meteo.com/v1/forecast?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": "LT-orai/1.1"})
    with urllib.request.urlopen(req, timeout=20) as response:
        result = json.load(response)
    if not isinstance(result, list) or len(result) != len(CITIES):
        raise ValueError("Netikėtas Open-Meteo atsakymo formatas")
    return result

def format_rows(result):
    rows = []
    for (name, _, _), item in zip(CITIES, result):
        current = item.get("current") or {}
        temp = current.get("temperature_2m")
        timestamp = current.get("time")
        code = current.get("weather_code")
        if not isinstance(temp, (int, float)) or not isinstance(timestamp, (int, float)):
            rows.append(f"| {name} | duomenų nėra | nenurodyta | — |")
            continue
        local = datetime.fromtimestamp(timestamp, timezone.utc).astimezone(
            ZoneInfo("Europe/Vilnius")).strftime("%Y-%m-%d %H:%M")
        rows.append(f"| {name} | {temp:g} °C | {CODES.get(code, 'nenurodyta')} | {local} |")
    return rows

def main():
    try:
        result = fetch()
        rows = format_rows(result)
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f"Nepavyko gauti aktualių Open-Meteo duomenų: {exc}", file=sys.stderr)
        return 1
    print("| Miestas | Temperatūra | Oro sąlygos | Laikas (Lietuvoje) |")
    print("|---|---:|---|---|")
    print("\n".join(rows))
    print("\nDuomenų tipas: dabartinės modeliuotos sąlygos, ne stočių matavimai.")
    print("Šaltinis: https://open-meteo.com/")
    print("Gauta:", datetime.now(ZoneInfo("Europe/Vilnius")).strftime("%Y-%m-%d %H:%M"), "(LT)")
    return 0

if __name__ == "__main__":
    sys.exit(main())
