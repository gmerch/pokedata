# Pokedata

## Setup

A few things to get set up. You should be able to run this form the traditional virtualenv setup, and installying requirements.txt. The only thing that won't work without your own .env fils the generateMNFSprites (that'll be renamed in the future, because it's an awful name). You need a directory pointing to a local instance of this [repo](https://github.com/msikma/pokesprite). Point it into 'pokemon-gen8/' and you should be good. I haven't fully implemented the shiny part of parsing on the Pokepaste, but that's because I'm lazy and it bears no difference on what I'm doing other than aesthetic.

## PasteParser

I swear one day I'll get better about documenting my side projects. In the mean time, I built this Pokepaste parser.
Specifically it's for a few key processes to make work for me. Every week I generate 10 teams from Pokesprites, and this process means that I no longer need to manually place all of the assets in the right spot in Illustrator. Yay!

