---
name: lt-orai
description: Pateikia užklausos metu aktualius penkių didžiausių Lietuvos miestų (Vilnius, Kaunas, Klaipėda, Šiauliai, Panevėžys) orus. ChatGPT režimu naudoja viešus interneto šaltinius be Python; Cursor / Codex gali paleisti Open-Meteo Python scenarijų. Naudoti, kai prašoma LT-orai ar Lietuvos miestų dabartinių orų.
---
# LT-orai

## Tikslas
Gauti šio iškvietimo metu naujausius pasiekiamus temperatūros ir oro sąlygų duomenis **Vilniui, Kaunui, Klaipėdai, Šiauliams ir Panevėžiui**. NENAUDOTI GitHub failuose saugomų senų temperatūrų ir neapsimesti, kad paieškos ištrauka yra tiesioginis matavimas.

## 1. ChatGPT režimas (numatytasis; be Python)

1. Kiekvieną kartą naudok prieinamą **interneto paieškos / atvėrimo arba orų duomenų priemonę**, o ne vien turimą modelio atmintį. Tikrink užklausos datos aktualumą ir kiekvieno miesto duomenų stebėjimo / atnaujinimo laiką.
2. Pirmasis šaltinis: viešas **Open-Meteo** dabartinių modeliuotų orų API:
   - Dokumentacija: https://open-meteo.com/en/docs
   - Viena penkių miestų užklausa (miestų eiliškumas sutampa su lentelės eilėmis):
     https://api.open-meteo.com/v1/forecast?latitude=54.6872%2C54.8985%2C55.7033%2C55.9349%2C55.7348&longitude=25.2797%2C23.9036%2C21.1443%2C23.3137%2C24.3575&current=temperature_2m%2Cweather_code&timezone=Europe%2FVilnius
   - Jei naršymo įrankis palaiko JSON: atsakyme tikėkis penkių objektų masyvo; iš kiekvieno imk `current.temperature_2m`, `current.weather_code` ir `current.time`. Jei `time` grąžinamas vietos laiku, papildomai jo nekonvertuok.
3. **Jei tiesioginis API JSON adresas užblokuotas naršymo įrankyje** (kai kurios ChatGPT naršyklės neleidžia atverti tokių adresų), NEbandyk to sutaisyti kodu ir nenutrauk: naudok įrankio orų funkciją arba viešų orų puslapių paiešką kiekvienam miestui. Pirmiausia bandyk viešą Lietuvos hidrometeorologijos tarnybos **HTML puslapį**: https://www.meteo.lt/prognozes/lietuvos-miestai/?area=vilnius (keisk `area` į `kaunas`, `klaipeda`, `siauliai`, `panevezys`). Įrankiuose, kurie grąžina tik paieškos rezultatus, ieškok `site:meteo.lt/prognozes/lietuvos-miestai area=kaunas valandinė prognozė` ir analogiškai kitiems miestams. Jei šis puslapis neprieinamas, naudok yr.no ar kitus patikimus puslapius, kuriuose aiškiai matomi miesto duomenys, vienetai ir aktualumo laikas. Vietovės prognozės papildomas šaltinis: https://api.meteo.lt/v1/places/vilnius/forecasts/long-term (keisk `vilnius` į `kaunas`, `klaipeda`, `siauliai`, `panevezys`).
4. Jei matai tik prognozę, aiškiai vadink ją **prognoze**, o ne dabartiniu matavimu. Nelygink skirtingų miestų istorinių ar skirtingų parų reikšmių kaip vienalaikių.
5. `weather_code` (WMO) kodus išversk pagal `scripts/orai.py` žodyną `CODES`; jei įrankis pateikia jau tekstinę sąlygą, naudok ją.
6. Sudaryk lietuvišką lentelę `Miestas | Temperatūra (°C) | Oro sąlygos | Duomenų laikas (LT) | Šaltinis / tipas`. Nurodyk užklausos datą ir šaltinių nuorodas. Jei kurios nors reikšmės negali patikimai patvirtinti, rašyk **„duomenų nėra“**. Neišgalvok reikšmių.
7. Jei pokalbyje jau pateikta pasenusi orų lentelė, naujam prašymui nevartok jos kaip aktualios – gauk naujus duomenis.

## 2. Cursor / Codex režimas (pasirinktinis)

Jei yra Python 3.9+ su interneto prieiga, repozitorijos šaknyje vykdyk:
```bash
python skills/lt-orai/scripts/orai.py
```
Programa pati kreipiasi į Open-Meteo ir atspausdina penkių miestų orus. Nereikia API rakto. Kai negalima paleisti programos, naudok 1 skyriaus interneto režimą.

## 3. Patikrinimas
Automatinį API integracijos testą GitHub Actions vykdo `.github/workflows/lt-orai-test.yml`. Jis tikrina Python kelią, bet **negarantuoja** kiekvieno ChatGPT naršymo įrankio galimybės atverti API JSON; todėl ChatGPT režime būtinas atsarginis viešų puslapių kelias. Testavimo scenarijai: `evals/evals.json`.
