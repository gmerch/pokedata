import os
import urllib.request
import re
from bs4 import BeautifulSoup
from PIL import Image
from .pokemon import Pokemon
from dotenv import load_dotenv


load_dotenv()
SPRITE_PATH = os.getenv('SPRITE_PATH')


def openURL(url):
    resp = urllib.request.urlopen(url)
    if resp.status == 200:
        return resp.read()
    raise BadURLException

def makeSoup(raw_html, encoder="lxml"):
    soup = BeautifulSoup(raw_html,features=encoder)
    return soup

def getPokemonList(soup):
    pokemon_list = soup.find_all('pre')
    return pokemon_list

def getPokemonSpecies(soup):
    if soup.span.text[:7] == 'Ability':
        # Check to see if the first 7 characaters of the span are Abiltiy
        if soup.text.find(' @') >= 0:
        # Check to see if there is an item or not
            name = soup.text[:soup.text.find(' @')].strip()
        else:
            name = soup[:soup.text.find('\n')].strip()
    else:
        name = soup.span.text
    return name

def getMoves(soup):
    progMove = re.compile('- (.*) \n')
    moves = [a.strip() for a in progMove.findall(soup.text)]
    return moves

def getAbility(soup):
    progAbility = re.compile('Ability: (.*) \n')
    ability = [a.strip() for a in progAbility.findall(soup.text)][0]
    return ability
    
def getItem(soup):
    progItem = re.compile('\@(.*) \n')
    item = [a.strip() for a in progItem.findall(soup.text)][0]
    return item

def getEVs(soup):
    evs_dict = {'HP':0,'Atk':0, 'Def':0,'SpA':0, 'SpD':0,'Spe':0}
    progEVs = re.compile('EVs: .* \n')
    evs = progEVs.findall(soup.text)
    if evs:
        evs = evs[0].strip()[5:].split(' / ')
    for ev in evs:
        val, key = ev.split(' ')
        evs_dict[key] = int(val)
    return evs_dict 

def getIVs(soup):
    ivs_dict = {'HP':31,'Atk':31, 'Def':31,'SpA':31, 'SpD':31,'Spe':31}
    progIVs = re.compile('IVs: .* \n')
    ivs = progIVs.findall(soup.text)
    if ivs:
        ivs = ivs[0].strip()[5:].split(' / ')
    for iv in ivs:
        val, key = iv.split(' ')
        ivs_dict[key] = int(val)
    return ivs_dict 

def getNature(soup):
    progNature = re.compile('(Hardy|Lonely|Brave|Adamant|Naughty|Bold|Docile|Relaxed|Impish|Lax|Timid|Hasty|Serious|Jolly|Naive|Modest|Mild|Quiet|Bashful|Rash|Calm|Gentle|Sassy|Careful|Quirky) Nature')
    nature = progNature.findall(soup.text)
    if nature:
        return nature[0]
    else:
        return "Serious Nature"


class BadUrlException(Exception):
    pass


class PasteParser:
    def __init__(self, paste):
        self.paste = paste
        self.html = openURL(self.paste)
        self.soup = makeSoup(self.html)

    def getPokemon(self,):
        self.html_pokemon = self.soup.find_all('pre')
        self.pokemon = []
        for pokemon in self.html_pokemon:
            name = getPokemonSpecies(pokemon)
            moves = getMoves(pokemon)
            ability = getAbility(pokemon)
            item = getItem(pokemon)
            evs = getEVs(pokemon)
            ivs = getIVs(pokemon)
            nature = getIVs(pokemon)
            self.pokemon.append(Pokemon(name,item,ability,evs,ivs,nature,moves))
    
    def generateMNFSprites(self, outpath, team_nm):
        # do something with opening images nad arranging them
        if not self.pokemon:
            self.getPokemon()
        paths = self.getSpritePaths()
        images = [Image.open(x) for x in paths]
        widths, heights = zip(*(i.size for i in images))
        total_width = int(sum(widths)/2)
        max_height = max(heights)*2
        image = Image.new('RGBA', (total_width, max_height))
        x_offset = 0
        y_offset = 0
        for i, im in enumerate(images):
            image.paste(im, (x_offset,y_offset))
            x_offset += im.size[0]
            if i == 2:
                x_offset = 0
                y_offset = max(heights)
        image.save(outpath+team_nm+'.png')

    def getSpritePaths(self,):
        paths = []
        for pokemon in self.pokemon:
            if pokemon.shiny:
                path = f'{SPRITE_PATH}shiny/{pokemon.pokemon}.png'
            else:
                path = f'{SPRITE_PATH}regular/{pokemon.pokemon}.png'
            paths.append(path)
        return paths



    def generateTeamSheet(self):
        print('not yet!')