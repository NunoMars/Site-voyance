from django.utils.translation import gettext as _
from random import shuffle as suf, choice, randint as rand
from .card_prints import one_card, clairvoyante_sort_cards

#faire Connaiscance
inputs = []
def clairvoyant(input_value):
        
    if input_value not in inputs:
        inputs.append(input_value)

    
    while True:
        #création deck
        card_deck = [i+1 for i in range(38)]    
        input_name = inputs[0]

        menu = {"messages" : "<div class='container' width = '100%'><div class='cta-inner text-center rounded'>" +
            "<div class='row'>" +
            "<div class='col'>" +
            "<p><h6 class='mb-0'>" + _("Muito obrigada ")  + input_name.capitalize() + " !</h6></p>" +
            "<p><h5 class='mb-0'>" + _(" Vou baralhando as cartas...") + "</h5></p></div></div>" +            
            "<div class='row'>" +
            "<div class='col'>" +
            "<p class='mb-0'><h5>" + _("Escolha o tema da pergunta!") + "</h5></p>" +
            "<p class='mb-0'><h6>" + _("Clique no baralho para escolher o baralho") + "</h6></p></div></div></div></div>" +
            "<div class='container' width = '100%'><div class='cta-inner text-center rounded'>" +
            "<div class='row'>" +
            "<div class='col'>" +
            "<p class='mb-0'><h6>" + _("AMOR") + "<h6></p>" +
            "<p><div class='mb-0'><input id='bouton_card' type='submit' class='bouton_card' onClick='sendMessageLove();'/></div></p></div>" +
            "<div class='col'>" +
            "<p class='mb-0'><h6>" + _("TRABALHO") + "</h6></p>" +
            "<p><div class='mb-0'><input id='bouton_card' type='submit' class='bouton_card' onClick='sendMessageWork();'/></div></p></div>" +
            "<div class='col'>" +
            "<p class='mb-0'><h6>" + _("GERAL") + "</h6></p>" +
            "<p><div class='mb-0'><input id='bouton_card' type='submit' class='bouton_card' onClick='sendMessageGen();'/></div></p></div>" +
            "<div class='col'>" +
            "<p class='mb-0'><h6>" + _("RAPIDA") + "</h6></p>" +
            "<p><div class='mb-0'><input id='bouton_card' type='submit' class='bouton_card' onClick='sendMessageOneCard();'/></div><p/>" +
            "</div></div></div></div>"
            } 

        if (len(inputs) == 1):
            return menu        
        
        if input_value == "one":
            card_deck = [i+1 for i in range(38)]
            suf(card_deck)
            rand_card = choice(card_deck)
            value = one_card(input_name, rand_card, menu)
            del inputs[1:]
            return value


        if (len(inputs) == 2):
            input_name = inputs[0]
            return {"messages" : "<div class='col'><div class='cta-inner text-center rounded'>" +
            "<p class='mb-0'><h4>" + _("Obrigada ") + input_name.capitalize() + " !</h4></p>" +
            " <p class='mb-0'>" + _("Estamos quase a saber o que o Tarot nos diz!") + "</p>" +
            " <p class='mb-0'>" + _("Clique no baralho para cortar en dois") + "</p>" +
            "<p class='mb-0'><input id='bouton_card' type='submit' class='bouton_card' onClick='sendMessageCut();'/></p>" +
            "</div>"
            }

        if input_value == "cut":
            cut_point = rand(1, 37)
            inputs[2] = cut_point
        
            return {"messages" : "<div class='col'><div class='cta-inner text-center rounded'>" +
            "<p class='mb-0'><h4>" + _("Obrigada !") + "</h4></p>" +
            "<p class='mb-0'>" + _("Temos, agora aqui os dois baralhos!") + "</p>" +
            "<p class='mb-0'>" + _("Clique no baralho para escolher o baralho") + "</p></div></div>" +
            "<div class='row'>" +
            "<div class='col''><div class='cta-inner text-center rounded'>" +
            "<div class='mb-0'><input id='bouton_card' type='submit' class='bouton_card' onClick='sendMessageLeft();'/></div></div></div>" +
            "<div class='col''><div class='cta-inner text-center rounded'>" +
            "<div class='mb-0'><input id='bouton_card' type='submit' class='bouton_card' onClick='sendMessageRight();'/></div></div></div>" +
            "</div>"
            }

        if inputs[1] == "love":
            print(inputs)                    
            result = clairvoyante_sort_cards(inputs[0], inputs[2], inputs[3], inputs[1], menu)
            del inputs[1:]
            print(inputs)
            return result                 

        if inputs[1] == "work":
            result = clairvoyante_sort_cards(inputs[0], inputs[2], inputs[3], inputs[1], menu)
            del inputs[1:]

            return result

        if inputs[1] == "gen":
            result = clairvoyante_sort_cards(inputs[0], inputs[2], inputs[3], inputs[1], menu)
            del inputs[1:]

            return result

        del inputs[1:]
        continue

