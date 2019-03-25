import unittest
import game.engine.dice as dice


class DiceRollTest(unittest.TestCase):
    def test_dice_roll(self):
        roll = dice.roll()
        self.assertGreaterEqual(roll, 1)
        self.assertLessEqual(roll, 6)
