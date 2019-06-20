import unittest
import game.character.creator as creator


class CreatorTestCase(unittest.TestCase):
    def test_character_name(self):
        hero = creator.new()
        self.assertEqual(hero.name, "Guido")
