"""데이터 무결성, 추출 계약 및 토너먼트 연동 검증."""

from collections import Counter
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

from src.food_loader import DATA_PATH, load_foods, sample_foods
from src.tournament import TournamentEngine


class FoodLoaderTests(unittest.TestCase):
    def test_dataset_integrity(self):
        data = json.loads(DATA_PATH.read_text(encoding="utf-8"))
        foods = load_foods()
        self.assertEqual(data["total_count"], 128)
        self.assertEqual(len(foods), 128)
        self.assertEqual({food["id"] for food in foods}, set(range(1, 129)))
        self.assertEqual(len({food["name"] for food in foods}), 128)
        self.assertEqual(len(data["categories"]), 4)
        self.assertEqual(
            Counter(food["category"] for food in foods),
            {category: 32 for category in data["categories"]},
        )
        for food in foods:
            for field in ("name", "category", "desc"):
                self.assertIsInstance(food[field], str)
                self.assertTrue(food[field].strip())

    def test_samples_and_tournament_integration(self):
        source = load_foods()
        self.assertEqual(len(sample_foods()), 32)
        for count in (8, 16, 32):
            with self.subTest(count=count):
                foods = sample_foods(count)
                self.assertEqual(len(foods), count)
                self.assertEqual(len({food["id"] for food in foods}), count)
                self.assertTrue(all(food in source for food in foods))
                engine = TournamentEngine(foods)
                while not engine.is_tournament_finished():
                    engine.advance_winner(engine.get_current_match()[0])
                self.assertEqual(len(engine.history), count - 1)
                self.assertIn(engine.get_final_champion(), foods)
        self.assertEqual(load_foods(), source)

    def test_invalid_counts(self):
        for count in (-1, 0, 7, 64, 129):
            with self.subTest(count=count), self.assertRaises(ValueError):
                sample_foods(count)
        for count in (True, False, 8.0, "8", None):
            with self.subTest(count=count), self.assertRaises(TypeError):
                sample_foods(count)

    def test_insufficient_foods(self):
        with patch("src.food_loader.load_foods", return_value=load_foods()[:7]):
            with self.assertRaises(ValueError):
                sample_foods(8)

    def test_script_from_another_directory(self):
        script = Path(__file__).resolve().parents[1] / "src" / "food_loader.py"
        with tempfile.TemporaryDirectory() as directory:
            result = subprocess.run(
                [sys.executable, str(script)], cwd=directory,
                capture_output=True, text=True, encoding="utf-8", check=True,
            )
        self.assertIn("32강 음식 비복원 추출 완료", result.stdout)
        self.assertEqual(len(result.stdout.splitlines()), 33)


if __name__ == "__main__":
    unittest.main()
