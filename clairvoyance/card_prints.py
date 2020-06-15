from random import shuffle as suf, randint as rand
from datetime import datetime
from .models import MajorArcana

card_deck = [i+1 for i in range(38)]

def one_card(input_value):
    rand_card = rand(0, 37)
    print(rand_card)
    obj = MajorArcana.objects.get(pk=rand_card)
    card_img = obj.card_image
    card_name = obj.card_name_pt
    card_warnings = obj.card_signification_warnings
    card_signification_gen = obj.card_signification_gen
    card_signification_love = obj.card_signification_love
    card_signification_work= obj.card_signification_work
    name= input_value

    return {"messages" : "<div class='container'><div class='cta-inner text-center rounded'>" +
        "<div class='col'><div class='cta-inner text-center rounded'>" +
        "<div class='mb-0'><h2>" + name.capitalize() + " o que o tarot tem para lhe dizer!</h2></div>" +
        "<div class='mb-0'><h3>" + card_name.capitalize() + "</h3></div>" +
        "<p class='mb-0'><a href= '#'><img src= " + card_img +
        " alt='card' height='25%' width='25%' /></a></p>" +
        "<div class='mb-0'><h4>" + "Significado en geral" + "</h4></div>" +
        "<p class='mb-0'>" + card_signification_gen + "</p>" +
        "<div class='mb-0'><h3>" + "Atenção" + "</h3></div>" +
        "<p class='mb-0'>" + card_warnings + "</p>" +
        "<div class='mb-0'><h4>" + "No amor" + "</h4></div>" +
        "<p class='mb-0'>" + card_signification_love + "</p>" +
        "<div class='mb-0'><h4>" + "No trabalho" + "</h4></div>" +
        "<p class='mb-0'>" + card_signification_work + "</p>" + 
        "</div></div> "}

def clairvoyante_sort_cards(name, cut_point, deck_chosed, chosed_theme):

    suf(card_deck)
    column = len(name)

    if deck_chosed == "left":
        chosen_deck = card_deck[0:cut_point]  

    if deck_chosed == "right":
        chosen_deck = card_deck[cut_point:37]

    if chosed_theme == 'love':
        chosed_theme = obj.card_signification_love
    
    if chosed_theme == 'work':
        chosed_theme = obj.card_signification_work
    
    if chosed_theme == 'gen':
        chosed_theme = obj.card_signification_gen

    #construire tableau
    def splitBy(li, n=1):
        return [li[i:i+n] for i in range(0, len(li), n)] 

    list_of_cards = []
    for i in chosen_deck:        
        obj = MajorArcana.objects.get(pk=i)
        card_img = obj.card_image
        card_name = obj.card_name_pt
        card_warnings = obj.card_signification_warnings
        print(card_warnings)
        list_of_cards.append(
            "<div class='col'><div class='cta-inner text-center rounded'>" +
            "<h6><div class='mb-0'>" + card_name.capitalize() + "</div></h6>" +
            "<p class='mb-0'><a href= '#'><img src= " + card_img +
            " alt='card' height='25%' width='25%' /><span>" + card_warnings +
            "</span></a></p>" +
            "<div class='mb-0'><h4>" + "No trabalho" + "</h4></div>" +
            "<p class='mb-0'>" + chosed_theme + "</p>" +
            "</div></div> "
        )

    card_board = splitBy(list_of_cards, column)
    final_card_deck = []
    for i in card_board:
        l = ''.join(i)
        final_card_deck.append("<div class='row' height= '100%' text-align='center'>" + l + "</div>")
    f = ''.join(final_card_deck)
    print(f)
    return {"messages" : "<div class='container'>" + 
    "<h4>Aqui esta o resultado das cartas</h4>" +
    "<h6>Para saber os avisos do Tarot passe o rato en cima de cada carta!</h6>" +
    f + "</div>"}
