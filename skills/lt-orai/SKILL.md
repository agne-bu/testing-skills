---
name: lt-orai
description: Pateikia dabartinę temperatūrą ir oro sąlygas Vilniuje, Kaune, Klaipėdoje, Šiauliuose ir Panevėžyje, naudodamas Open-Meteo API. Naudok, kai vartotojas prašo LT-orai, Lietuvos penkių didžiausių miestų orų ar jų temperatūrų palyginimo.
---
# LT-orai

1. Penki miestai fiksuoti: Vilnius, Kaunas, Klaipėda, Šiauliai, Panevėžys.
2. Pagrindinis ir vienintelis šio įgūdžio duomenų šaltinis: Open-Meteo Forecast API, https://open-meteo.com/en/docs. Jis teikia modeliuotas dabartines sąlygas, o ne tiesioginius meteorologinių stočių matavimus.
3. Jei galima vykdyti Python su interneto prieiga, iš įgūdžio katalogo paleisk `python scripts/orai.py`. Programa naudoja tik standartinę Python biblioteką (rekomenduojama Python 3.9+ ir veikiančios laiko juostų duomenų bazės).
4. Jei Python negalima paleisti, interneto priemonėmis užklausk `https://api.open-meteo.com/v1/forecast`, nurodyk penkių miestų koordinates iš `scripts/orai.py`, parametrus `current=temperature_2m,weather_code`, `timezone=Europe/Vilnius` ir `timeformat=unixtime`. API grąžina penkių objektų masyvą ta pačia koordinačių tvarka.
5. `weather_code` yra WMO kodas. Versk jį pagal `scripts/orai.py` esantį `CODES` žodyną; nežinomą kodą žymėk „nenurodyta“.
6. Parodyk lentelę „Miestas | Temperatūra | Oro sąlygos | Laikas (Lietuvoje)“. Naudok API grąžintą `current.time` ir konvertuok iš Unix UTC į Europe/Vilnius. Nevadink šių duomenų faktiniais matavimais.
7. Nurodyk šaltinį ir užklausos laiką. Jei API neveikia arba laukai trūksta, nekurk išgalvotų reikšmių; pažymėk „duomenų nėra“.
8. Nenaudok ankstesnio meteo.lt API kodo. Testavimo scenarijai: `evals/evals.json`.
