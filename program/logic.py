from random import shuffle as suf
from pprint import pprint as pp

print("Bonjour je vais te faire un tirage personalisé rien que pour toi!!")
print("concentre-toi on commence!")

#faire Connaiscance
first_name = input("Quel est ton prénon? ")

print("Plaisir de faire ta connaissance " + first_name + " !")

birth_date = input("Ta date de naissance? ")

#création deck
card_deck = [i+1 for i in range(38)]

#mélanger deck
suf(card_deck)
print(card_deck)

#couper deck
while True:
    deck_cuted = int(input("Maintenant, ecrivez un chiffre de 1 a 38 svp et appuyez sur entree! "))
    if deck_cuted in card_deck:
        break
    else:
        continue
right_deck = card_deck[0:deck_cuted]
left_deck = card_deck[deck_cuted:38]
print(right_deck)
print(left_deck)

column = len(first_name)
print(column)
while True:
    deck_choice = input("On a donc deux tas tu choisis celui de droite ou de gauche ?")
    if deck_choice == "droite" or "Droite":
        chosen_deck = right_deck
        break
    if deck_choice == "gauche" or "Gauche":
        chosen_deck = left_deck
        break
    else:
        continue

#construire tableau
def splitBy(li, n=1):
    return [li[i:i+n] for i in range(0, len(li), n)]

card_board = splitBy(chosen_deck, column)
pp(card_board)
