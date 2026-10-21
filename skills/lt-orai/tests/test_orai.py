"""Offline tests for LT-orai formatting; run with python -m unittest discover."""
import importlib.util
import pathlib
import unittest
from datetime import datetime, timezone

ROOT = pathlib.Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("lt_orai", ROOT / "scripts" / "orai.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

class TestWeather(unittest.TestCase):
    def test_all_cities_and_wmo_translation(self):
        ts = int(datetime(2026, 10, 21, 12, tzinfo=timezone.utc).timestamp())
        data = [{"current": {"temperature_2m": 10.5, "weather_code": 3, "time": ts}} for _ in range(5)]
        rows = mod.format_rows(data)
        self.assertEqual(len(rows), 5)
        self.assertTrue(all("10.5 °C" in r and "debesuota" in r for r in rows))
        self.assertIn("15:00", rows[0])

    def test_missing_data_not_fabricated(self):
        rows = mod.format_rows([{"current": {}} for _ in range(5)])
        self.assertTrue(all("duomenų nėra" in r for r in rows))

if __name__ == "__main__":
    unittest.main()
