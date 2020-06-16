from django.utils.translation import gettext as _
from random import shuffle as suf, randint as rand
from .card_prints import one_card, clairvoyante_sort_cards

#faire Connaiscance
inputs = []
def clairvoyant(input_value):
    while True:
        #création deck
        card_deck = [i+1 for i in range(38)]    
        
        if input_value not in inputs:
            inputs.append(input_value)
            print(inputs)

        input_name = inputs[0]
        
        if (len(inputs) == 1):        

            msg = {"messages" : "<div class='container' width = '100%'><div class='cta-inner text-center rounded'>" +
            "<div class='row'>" +
            "<div class='col'>" +
            "<p><h6 class='mb-0'>" + _("Muito obrigada ")  + input_value.capitalize() + " !</h6></p>" +
            "<p><h5 class='mb-0'>" + _(" Vou baralhando as cartas...") + "</h5></p></div></div>" +            
            "<div class='row'>" +
            "<div class='col'>" +
            "<p class='mb-0'><h5>" + _("Escolha o tema da pergunta!") + "</h5></p>" +
            "<p class='mb-0'><h6>" + _("Clique no baralho para escolher o baralho") + "</h6></p></div></div></div></div>" +
            "<div class='container' width = '100%'><div class='cta-inner text-center rounded'>" +
            "<div class='row'>" +
            "<div class='col'>" +
            "<p class='mb-0'><h8>" + _("AMOR") + "<h8></p>" +
            "<p><div class='mb-0'><input id='bouton_card' type='submit' class='bouton_card' onClick='sendMessageLove();'/></div></p></div>" +
            "<div class='col'>" +
            "<p class='mb-0'><h8>" + _("TRABALHO") + "</h8></p>" +
            "<p><div class='mb-0'><input id='bouton_card' type='submit' class='bouton_card' onClick='sendMessageWork();'/></div></p></div>" +
            "<div class='col'>" +
            "<p class='mb-0'><h8>" + _("GERAL") + "</h8></p>" +
            "<p><div class='mb-0'><input id='bouton_card' type='submit' class='bouton_card' onClick='sendMessageGen();'/></div></p></div>" +
            "<div class='col'>" +
            "<p class='mb-0'><h8>" + _("RAPIDA") + "</h8></p>" +
            "<p><div class='mb-0'><input id='bouton_card' type='submit' class='bouton_card' onClick='sendMessageOneCard();'/></div><p/>" +
            "</div></div></div></div>"
            } 

            return msg

        while True:

            if inputs[1] == "one":
                input_name = inputs[0]
                value = one_card(input_name)
                return value

            else:
                if (len(inputs) == 2):

                    return {"messages" : "<div class='col'><div class='cta-inner text-center rounded'>" +
                    "<p class='mb-1'><h4>" + _("Obrigada !") + "</h4></p>" +
                    " <p class='mb-1'>" + _("Estamos quase a saber o que o Tarot nos diz!") + "</p>" +
                    " <p class='mb-1'>" + _("Clique no baralho para cortar en dois") + "</p>" +
                    "<p class='mb-1'><input id='bouton_card' type='submit' class='bouton_card' onClick='sendMessageCut();'/></p>" +
                    "</div>"
                    }

                if inputs[2] == "cut":
                    cut_point = rand(0, 37)

                if (len(inputs) == 3):
                    
                    return {"messages" : "<div class='container'><div class='cta-inner text-center rounded'>" +
                    "<div class='row' height= '100%' text-align='center'>" +
                    "<p class='mb-1'>" + _("Obrigada !") + "</p>" +
                    " <p class='mb-1'>" + _("Temos aqui os dois baralhos!") + "</p>" +
                    " <p class='mb-1'>" + _("Clique no baralho para escolher o baralho") + "</p></div>" +
                    "<div class='row' height= '100%' text-align='center'>" +
                    "<div class='col''><input id='bouton_card' type='submit' class='bouton_card' onClick='sendMessageLeft();'/></div>" +
                    "<div class='col''><input id='bouton_card' type='submit' class='bouton_card' onClick='sendMessageRight();'/></div>" +
                    "</div></div>"
                    }

                deck_chosed = inputs[3]       

                if inputs[1] == "love":                    
                    result = clairvoyante_sort_cards(input_name, cut_point, deck_chosed,"love")
                    return result                 

                if inputs[1] == "work":
                    result = clairvoyante_sort_cards(input_name, cut_point, deck_chosed,"work")
                    return result

                if inputs[1] == "gen":
                    result = clairvoyante_sort_cards(input_name, cut_point, deck_chosed,"gen")
                    return result
            break
        del inputs[1:]
        continue

