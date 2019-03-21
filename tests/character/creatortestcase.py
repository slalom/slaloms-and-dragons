import unittest
import character.creator


class CreatorTestCase(unittest.TestCase):
    def test_character_name(self):
        hero = character.creator.new()
        self.assertEqual(hero.name, 'Guido')