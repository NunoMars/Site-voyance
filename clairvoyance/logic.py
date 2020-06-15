from random import shuffle as suf, randint as rand
from .card_prints import one_card, clairvoyante_sort_cards

#faire Connaiscance
inputs = []
def clairvoyant(input_value):
    #création deck
    card_deck = [i+1 for i in range(38)]

    
    if input_value not in inputs:
        inputs.append(input_value)
        print(inputs)

    """while True:
        del inputs[1:]"""

    if (len(inputs) == 1):        

        msg = {"messages" : "<div class='col'><div class='cta-inner text-center rounded'>" +
        "<p class='mb-1'>Muito obrigada " + input_value.capitalize() + " !" +
        " Vou baralhando as cartas..." +
        "<div class='container'><div class='cta-inner text-center rounded'>" +
        "<div class='col' height= '100%' text-align='center'>" +
        "<p class=class='mb-0'>Escolha o tema da pergunta!</p>" +
        "<p class=class='mb-0'>Clique no baralho para escolher o baralho</p></div>" +
        "<div class='row' height= '100%' text-align='center'>" +
        "<p class=class='mb-0'><h6>" + "Pergunta sobre AMOR" + "<h6></p>"
        "<p><div class='col''><input id='bouton_card' type='submit' class='bouton_card' onClick='sendMessageLove();'/></div></p>" +
        "<p class=class='mb-0'><h6>" + "Pergunta sobre TRABALHO" + "</h6></p>"
        "<p><div class='col''><input id='bouton_card' type='submit' class='bouton_card' onClick='sendMessageWork();'/></div></p>" +
        "<p class=class='mb-0'><h6>" + "Pergunta sobre SITUACAO EN GERAL" + "</h6></p>"
        "<p><div class='col''><input id='bouton_card' type='submit' class='bouton_card' onClick='sendMessageGen();'/></div></p>" +
        "<p class=class='mb-0'><h6>" + "Pergunta RAPIDA (una carta)" + "</h6></p>"
        "<p><div class='col''><input id='bouton_card' type='submit' class='bouton_card' onClick='sendMessageOneCard();'/></div><p/>" +
        "</div></div>"
        } 

        return msg

    if inputs[1] == "one":
        input_name = inputs[0]
        value = one_card(input_name)
        return value
        del inputs[1:]
        
    else:
        if (len(inputs) == 2):

            return {"messages" : "<div class='col'><div class='cta-inner text-center rounded'>" +
            "<p class='mb-1'>Obrigada !</p>" +
            " <p class='mb-1'>Estamos quase a saber o que o Tarot nos diz!</p>" +
            " <p class='mb-1'>Clique no baralho para cortar en dois</p>" +
            "<p class='mb-1'><input id='bouton_card' type='submit' class='bouton_card' onClick='sendMessageCut();'/></p>" +
            "</div>"
            }

        if (len(inputs) == 3):
            
            return {"messages" : "<div class='container'><div class='cta-inner text-center rounded'>" +
            "<div class='row' height= '100%' text-align='center'>" +
            "<p class='mb-1'>Obrigada !</p>" +
            " <p class='mb-1'>Temos aqui os dois baralhos!</p>" +
            " <p class='mb-1'>Clique no baralho para escolher o baralho</p></div>" +
            "<div class='row' height= '100%' text-align='center'>" +
            "<div class='col''><input id='bouton_card' type='submit' class='bouton_card' onClick='sendMessageLeft();'/></div>" +
            "<div class='col''><input id='bouton_card' type='submit' class='bouton_card' onClick='sendMessageRight();'/></div>" +
            "</div></div>"
            }

        deck_chosed = inputs[3]       

        if input_value[1] == "love":
            result = clairvoyante_sort_cards(input_name, cut_point, deck_chosed,"love")
            return result
        if input_value[1] == "work":
            result = clairvoyante_sort_cards(input_name, cut_point, deck_chosed,"work")
            return result
        if input_value[1] == "gen":
            result = clairvoyante_sort_cards(input_name, cut_point, deck_chosed,"gen")
            return result


