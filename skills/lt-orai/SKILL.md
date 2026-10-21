---
name: lt-orai
description: "LT-orai: paleisk, kai vartotojas parašo „panaudok LT-orai“, „LT-orai“, „parodyk LT-orai“ ar paprašo dabartinių penkių didžiausių Lietuvos miestų orų. Kiekvieną kartą interneto naršymo priemone skaityk naują Vilniaus, Kauno, Klaipėdos, Šiaulių ir Panevėžio valandinę prognozę iš meteo.lt HTML puslapių; Python ir API nereikia."
---
# LT-orai

## Iškvietimas

**Trigeris:** jei vartotojas parašo tik „panaudok LT-orai“ (taip pat „LT-orai“), iš karto atlik visus toliau pateiktus žingsnius ir pateik lentelę. Neprašyk pakartoti instrukcijų ar GitHub adreso. Šis įgūdis skirtas vykdyti pokalbyje, ne vien pateikti naudojimo paaiškinimą.

## ChatGPT režimas: tik vieši HTML puslapiai, be Python

**Svarbiausia:** ChatGPT režime **NEKREIPKIS į Open-Meteo API** ir **NEPALEISK `scripts/orai.py`**. Šiose aplinkose tiesioginis API domenas ar Python tinklas gali būti nepasiekiami. Vietoj to kiekvieną kartą naudok turimą **interneto naršymo / paieškos įrankį** ir perskaityk penkių miestų **meteo.lt HTML valandinių prognozių** puslapius.

Pagrindinis ir tiesiogiai ChatGPT naršymo įrankiu patikrintas šaltinis – Lietuvos hidrometeorologijos tarnyba, 2026-10-21 patikrinti visi penki puslapiai:
- Vilnius: https://www.meteo.lt/prognozes/lietuvos-miestai/?area=vilnius
- Kaunas: https://www.meteo.lt/prognozes/lietuvos-miestai/?area=kaunas
- Klaipėda: https://www.meteo.lt/prognozes/lietuvos-miestai/?area=klaipeda
- Šiauliai: https://www.meteo.lt/prognozes/lietuvos-miestai/?area=siauliai
- Panevėžys: https://www.meteo.lt/prognozes/lietuvos-miestai/?area=panevezys

### Veiksmai

1. Nustatyk tikrą užklausos datą ir Lietuvos laiką (`Europe/Vilnius`).
2. Interneto įrankiu atidaryk kiekvieną aukščiau pateiktą puslapį; jei reikia, ieškok puslapio pagal `site:meteo.lt/prognozes/lietuvos-miestai/ "Vilnius" valandinė prognozė` (ir kitus miestus), bet **nepasikliauk pasenusia paieškos ištrauka**.
3. Kiekviename puslapyje patikrink, ar rodoma **einamoji kalendorinė diena**. Iš lentelės „Valandinė prognozė“ paimk arčiausiai einamojo Lietuvos laiko esančią valandą, jos `Temperatūra` (°C) ir `Reiškinys` (tekstą, kuris gali būti paveikslėlio alt apraše).
4. Jei puslapis pateikia vakarykščius ar senesnius duomenis, nenaudok jų kaip dabartinių. Jei prognozė šiai valandai jau neberodoma, pasirink artimiausią būsimą valandą ir aiškiai ją nurodyk.
5. Pateik vieną lentelę `Miestas | Temperatūra, °C | Oro sąlygos | Prognozės data ir laikas (LT)`. **Tai prognozė, ne meteorologinės stoties matavimai.** Visus duomenis paimk iš šio iškvietimo metu atvertų šaltinių, ne iš ankstesnės žinutės.
6. Po lentele nurodyk „Šaltinis: Lietuvos hidrometeorologijos tarnyba (meteo.lt)“ ir nuorodas/citatas į patikrintus puslapius.
7. Jei atverti puslapį nepavyksta, bandyk kitą viešą **HTML** orų puslapį (pvz., yr.no). Jei nėra tikrinamų dabartinės datos duomenų, rašyk `duomenų nėra` ir tiksliai nurodyk priežastį. **Nekeisk maršruto į Open-Meteo API ir nerodyk senų skaičių.**

## Cursor / Codex režimas (atskiras; pasirinktinis)

Jei vartotojas aiškiai pageidauja Python ar lokalaus scenarijaus, repozitorijos šaknyje vykdyk `python skills/lt-orai/scripts/orai.py`. Šis failas naudoja Open-Meteo ir nėra ChatGPT režimo dalis. GitHub Actions tikrina Python / API scenarijų, o ne HTML naršymo režimą.

## Svarbi naudojimo riba

Šis failas yra GitHub saugoma instrukcija. ChatGPT turi jį perskaityti per GitHub jungtį; vien pavadinimas `LT-orai` neįdiegia ir automatiškai neaktyvuoja įgūdžio ChatGPT įgūdžių kataloge.
