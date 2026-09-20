"""
Unit tests for FoodWorldCupGame in src/game.py
Authored by: Ahn Jaehyun (Lead Architect)
"""

import unittest
from src.game import FoodWorldCupGame


class TestFoodWorldCupGame(unittest.TestCase):
    def test_game_initialization(self):
        game = FoodWorldCupGame(round_size=8, players=["플레이어A", "플레이어B"])
        self.assertEqual(game.round_size, 8)
        self.assertEqual(len(game.foods), 8)
        self.assertEqual(game.engine.current_round_name, "8강")

    def test_game_invalid_round_size(self):
        with self.assertRaises(ValueError):
            FoodWorldCupGame(round_size=10)

    def test_run_simulation_completes_and_returns_champion(self):
        game = FoodWorldCupGame(round_size=8, players=["A", "B", "C"])
        champion = game.run_simulation(random_seed=42)
        self.assertIsNotNone(champion)
        self.assertIn("name", champion)
        self.assertIn("category", champion)
        self.assertTrue(game.engine.is_tournament_finished())


if __name__ == "__main__":
    unittest.main()