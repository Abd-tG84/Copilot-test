import unittest
from calculator.dice import Dice

class TestDice(unittest.TestCase):
    def test_roll_with_default_sides(self):
        dice = Dice()
        result = dice.roll()
        self.assertTrue(1 <= result <= 6)

    def test_roll_with_custom_sides(self):
        dice = Dice(sides=12)
        result = dice.roll()
        self.assertTrue(1 <= result <= 12)

    def test_invalid_sides(self):
        with self.assertRaises(ValueError):
            Dice(sides=0)

if __name__ == "__main__":
    unittest.main()