'''
This file contains functions for parsing txt files with deck information
'''
from pprint import pprint

def parse(deck_file_name):
    '''
    turns text file into a deck(list of card dictionaries)
    expects text file  like:
    2 cardName1
    1 cardName2
    '''
    side = False
    main = []
    sideboard = [] 
    deck = {'deck' : main, 'sideboard' : sideboard}
    with open(deck_file_name, 'r') as deck_file:
        for line in deck_file:
            line = line.lower().strip().split(' ',1)
            if len(line) == 1:
                if line[0] == 'sideboard':
                    side = True
            else:
                name = line[1]
                quantity = line[0]
                card = {
                    'name': name,
                    'quantity': quantity
                }
                if side:
                    sideboard.append(card)
                else:
                    main.append(card)
    pprint(deck)
    return deck

parse('sampledata/scg_grag_3.txt')

