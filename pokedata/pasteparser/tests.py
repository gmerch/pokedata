import unittest

from pasteparser import *

class TestParserMethods(unittest.TestCase):

    def test_open(self):
        self.assertIsNotNone(openURL('https://pokepast.es/a4534e4d9efab9b7'))

    def test_soup(self):
        self.assertIsNotNone(makeSoup(openURL('https://pokepast.es/a4534e4d9efab9b7')))

    def test_pokemon_list(self):
        self.assertEqual(len(getPokemonList(makeSoup(openURL('https://pokepast.es/a4534e4d9efab9b7')))),6)

    def test_pokemon_species(self):
        html = openURL('https://pokepast.es/a4534e4d9efab9b7')
        soup = makeSoup(html)
        pokemon_list = getPokemonList(soup)
        self.assertEqual(getPokemonSpecies(pokemon_list[0]),'Garchomp')

    def test_pokemon_moves(self):
        html = openURL('https://pokepast.es/a4534e4d9efab9b7')
        soup = makeSoup(html)
        pokemon_list = getPokemonList(soup)
        moves = getMoves(pokemon_list[0])
        self.assertEqual(len(moves),4)
        self.assertEqual(moves[0],'Protect')

    def test_pokemon_abilities(self):
        html = openURL('https://pokepast.es/a4534e4d9efab9b7')
        soup = makeSoup(html)
        pokemon_list = getPokemonList(soup)
        ability = getAbility(pokemon_list[0])
        self.assertEqual(ability,'Rough Skin')

    def test_pokemon_items(self):
        html = openURL('https://pokepast.es/a4534e4d9efab9b7')
        soup = makeSoup(html)
        pokemon_list = getPokemonList(soup)
        item = getItem(pokemon_list[0])
        self.assertEqual(item,'Lum Berry')

if __name__ == '__main__':
    unittest.main()