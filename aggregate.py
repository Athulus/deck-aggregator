'''
This file will impliment the deck aggreagation algorithm
'''
from pprint import pprint
from parse import parse
# metacard = {
#     'name': , # card name
#     'instance': , #nth card in deck
#     'count': , #total number of this card instance in all decks
# }
def aggregate(decks):
    '''
    params:
        decks - list of deck dictionaries
    returns:
        the aggregated deck list from the list of decks provided
    steps:
    1. seperate decks into numbered cards
    2. aggreagate all cardsinto one list
    3. sort by quantity
    4. pick first 60 cards
    5. repeat with sideboard?
    '''
    main_decks = []
    sideboards = []
    agg = {'deck' : [], 'sideboard' : []}
    for deck in decks:
        sideboards.append(deck[sideboard])
        main_decks.append(deck[deck])
    main_deck = combine_cards(main_decks)
    sideboard = combine_cards(sideboards)

    main_deck.sort()
    sideboard.sort()

    main_deck = main_deck[:60]
    sideboard = sideboard[:15]

    return agg

def combine_cards(decks):
    return decks[0]

def main():
    ''' for testing'''
    filename = ''
    decks = parse(filename)
    agg_deck = aggregate(decks)
    pprint(agg_deck)
