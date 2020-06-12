from random import shuffle as suf
from .models import MajorArcana

#faire Connaiscance
def clairvoyant(first_name, birth, number, right_or_left):
    #création deck
    card_deck = [i+1 for i in range(38)]

    #mélanger deck
    suf(card_deck)

    #couper deck
    while True:
        if number in card_deck:
            break
        else:
            continue
    right_deck = card_deck[0:number]
    left_deck = card_deck[number:38]
    print(right_deck)
    print(left_deck)

    column = len(first_name)
    print(column)
    while True:
        if right_or_left == "droite" or "Droite":
            chosen_deck = right_deck
            break
        if right_or_left == "gauche" or "Gauche":
            chosen_deck = left_deck
            break
        else:
            continue

    #construire tableau
    def splitBy(li, n=1):
        return [li[i:i+n] for i in range(0, len(li), n)]

    card_board = splitBy(chosen_deck, column)
    return card_board

