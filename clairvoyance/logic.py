from django.utils.translation import gettext as _
from random import shuffle as suf, choice, randint as rand
from .card_prints import one_card, clairvoyante_sort_cards


inputs = []


def clairvoyant(input_value):
    """
        Construct the bot reponse.
    """
    card_deck = [i+1 for i in range(38)]
    global inputs
    if input_value not in inputs:
        inputs.append(input_value)
    print(inputs)

    while True:
        # création deck
        if input_value == "Quit":
            del inputs[0:]

        menu = {"messages": "<div class='cta-inner text-center rounded'>" +
                "<div class='row'>" +
                "<div class='col'>" +
                "<p><h6>" + _("Muito obrigada ") + inputs[0].capitalize() + " !</h6></p>" +
                "<p><h5>" + _(" Vou baralhando as cartas...") + "</h5></p></div></div>" +
                "<div class='row'>" +
                "<div class='col'>" +
                "<p><h5>" + _("Escolha o tema da pergunta!") + "</h5></p>" +
                "<p><h6>" + _("Clique no baralho para escolher o baralho") + "</h6></p></div></div>" +
                "<div class='row'>" +
                "<div class='col'>" +
                "<p><h6>" + _("AMOR") + "<h6></p>" +
                "<p><input id='bouton_card' type='submit' class='bouton_card' onClick='sendMessageLove();'/></p></div>" +
                "<div class='col'>" +
                "<p><h6>" + _("TRABALHO") + "</h6></p>" +
                "<p><input id='bouton_card' type='submit' class='bouton_card' onClick='sendMessageWork();'/></p></div>" +
                "<div class='col'>" +
                "<p><h6>" + _("GERAL") + "</h6></p>" +
                "<p><input id='bouton_card' type='submit' class='bouton_card' onClick='sendMessageGen();'/></p></div>" +
                "<div class='col'>" +
                "<p><h6>" + _("RAPIDA") + "</h6></p>" +
                "<p><input id='bouton_card' type='submit' class='bouton_card' onClick='sendMessageOneCard();'/></p></div>" +
                "</div></div>"
                }

        if input_value == "one":
            card_deck = [i+1 for i in range(38)]
            suf(card_deck)
            rand_card = choice(card_deck)
            value = one_card(inputs[0], rand_card, menu)
            del inputs[1:]
            return value

        if (len(inputs) == 1):
            return menu

        if input_value == "love":
            inputs[1] = "love"

        if input_value == "work":
            inputs[1] = "work"

        if input_value == "gen":
            inputs[1] = "gen"

        if (len(inputs) == 2):
            input_name = inputs[0]
            return {"messages": "<div class='cta-inner text-center rounded'>" +
                    "<div class='row'>" +
                    "<div class='col'>" + 
                    "<p><h4>" + _("Obrigada ") + input_name.capitalize() + " !</h4></p>" +
                    " <p>" + _("Estamos quase a saber o que o Tarot nos diz!") + "</p>" +
                    " <p>" + _("Clique no baralho para cortar en dois") + 
                    "</p></div></div>" +
                    "<div class='row'>" +
                    "<div class='col'>" + 
                    "<input id='bouton_card' type='submit' class='bouton_card' onClick='sendMessageCut();'/></div>" +
                    "</div></div></div>"
                    }

        if input_value == "cut":
            cut_point = rand(1, 37)
            inputs[2] = cut_point
            left_deck = card_deck[0:cut_point]
            right_deck = card_deck[cut_point:37]

            return {"messages": "<div class='col'><div class='cta-inner text-center rounded'>" +
                    "<p class='mb-0'><h4>" + _("Obrigada !") + "</h4></p>" +
                    "<p class='mb-0'>" + _("Temos, agora aqui os dois baralhos!") + "</p>" +
                    "<p class='mb-0'>" + _("Clique no baralho para escolher o baralho") + "</p></div></div>" +
                    "<div class='row'>" +
                    "<div class='col''><div class='cta-inner text-center rounded'>" +
                    "<h1>Este baralho tem " + str(len(left_deck)) + " cartas!" +
                    "<div class='mb-0'><input id='bouton_card' type='submit' class='bouton_card' onClick='sendMessageLeft();'/></div></div></div>" +
                    "<div class='col''><div class='cta-inner text-center rounded'>" +
                    "<h1>Este baralho tem " + str(len(right_deck)) + " cartas!" +
                    "<div class='mb-0'><input id='bouton_card' type='submit' class='bouton_card' onClick='sendMessageRight();'/></div></div></div>" +
                    "</div>"
                    }

        # chose the deck
        if input_value == "left":
            inputs[3] = card_deck[0:inputs[2]]

        if input_value == "right":
            inputs[3] = card_deck[inputs[2]:37]

        result = clairvoyante_sort_cards(inputs[0], inputs[3], inputs[1], menu)
        del inputs[1:]
        return result
