---
name: lt-orai
description: Pateikia naujausią oro temperatūrą ir sąlygas penkiuose didžiausiuose Lietuvos miestuose iš oficialaus meteo.lt šaltinio. Naudok, kai prašoma „LT-orai“, „LT orai“, orų penkiuose didžiausiuose miestuose arba Lietuvos didmiesčių temperatūrų palyginimo.
---
# LT-orai

1. Pateik Vilnių, Kauną, Klaipėdą, Šiaulius ir Panevėžį tokia tvarka.
2. Naudok oficialią Lietuvos hidrometeorologijos tarnybos API `https://api.meteo.lt/v1/`. Jei yra galimybė vykdyti Python su tinklo prieiga, paleisk `python scripts/orai.py` iš šio įgūdžio katalogo. Kitu atveju užklausk API turimomis interneto priemonėmis.
3. Pirmiausia imk naujausius faktinius matavimus iš `/stations/{station-code}/observations/latest`: vilniaus-ams, kauno-ams, klaipedos-ams, siauliu-ams, panevezio-ams. Patikrink stočių kodus pagal `/stations`, jei užklausa grąžina klaidą. Imk įrašą su naujausia `observationTimeUtc`, kuriame yra `airTemperature`.
4. Jei miesto faktinio matavimo nėra, naudok `/places/{place-code}/forecasts/long-term`, pasirink artimiausią prognozės laiką, kuris nėra ankstesnis už dabartinį UTC laiką. Nevadink prognozės faktiniu matavimu.
5. `conditionCode` versk į lietuvių kalbą pagal `references/conditions.md`. Jei sąlyga nežinoma ar null, rašyk „nenurodyta“.
6. Pateik kompaktišką lentelę: Miestas | Temperatūra (°C) | Oro sąlygos | Duomenų tipas | Laikas (Lietuvos laiku). Laiką konvertuok į Europe/Vilnius, įvertindamas vasaros laiką. Jei vienam miestui duomenų nėra, rašyk „duomenų nėra“, neišgalvok.
7. Po lentele nurodyk šaltinį: Lietuvos hidrometeorologijos tarnyba, https://meteo.lt/ ir duomenų gavimo laiką. Nenaudok senų atsakymų kaip aktualių duomenų.
8. Jei API nepasiekiama, aiškiai pranešk, kad aktualių duomenų patvirtinti nepavyko.
