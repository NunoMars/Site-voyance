from random import shuffle as suf, choice, randint as rand
from django.utils.translation import gettext as _
from datetime import datetime
from .models import MajorArcana


def get_from_db(id_card):
    """
        Get objects from DataBase
    """
    obj = MajorArcana.objects.get(pk=id_card)
    card_img = obj.card_image
    card_name = obj.card_name_pt
    card_warnings = obj.card_signification_warnings
    card_signification_gen = obj.card_signification_gen
    card_signification_love = obj.card_signification_love
    card_signification_work = obj.card_signification_work
    card_polarity = obj.card_polarity
    return [
        card_img,
        card_name,
        card_warnings,
        card_signification_gen,
        card_signification_love,
        card_signification_work,
        card_polarity
    ]


def one_card(name, rand_card, menu):
    """
        Rends one cart reponse.
    """
    card = get_from_db(rand_card)

    return {"messages": "<div class='container'><div class='cta-inner text-center rounded'>" +
            "<div class='col'><div class='cta-inner text-center rounded'>" +
            "<div class='mb-0'><h2>" + name.capitalize() + _(" o que o tarot tem para lhe dizer!") + "</h2></div>" +
            "<div class='mb-0'><a href='#'><img src='/static/img/cards/Back.jpg'" +
            "onmouseover=" + '"this.src=' + "'" + card[0] + "'" + '"' +
            "border='0' alt='' height='25%' width='25%'/></a></div>" +
            "<div class='mb-0'><h3>" + _(card[1].capitalize()) + "</h3></div>" +
            "<div class='mb-0'><h3>" + _("Atenção") + "</h3></div>" +
            "<p class='mb-0'>" + _(card[2]) + "</p>" +
            "<div class='mb-0'><h4>" + _("Significado en geral") + "</h4></div>" +
            "<p class='mb-0'>" + _(card[3]) + "</p>" +
            "<div class='mb-0'><h4>" + _("No amor") + "</h4></div>" +
            "<p class='mb-0'>" + _(card[4]) + "</p>" +
            "<div class='mb-0'><h4>" + _("No trabalho") + "</h4></div>" +
            "<p class='mb-0'>" + _(card[5]) + "</p>" +
            "</div></div></div></div> " + menu["messages"]
            }


def response_card(name, index_result_card, chosed_theme, menu):

    card = get_from_db(index_result_card)
    if chosed_theme == "love":
        chosed_theme = card[4]
    if chosed_theme == "work":
        chosed_theme = card[5]
    if chosed_theme == "gen":
        chosed_theme = card[3]

    return {"messages": "<div class='container'><div class='cta-inner text-center rounded'>" +
            "<div class='col'><div class='cta-inner text-center rounded'>" +
            "<div class='mb-0'><h2>" + name.capitalize() + _(" o que o tarot tem para lhe dizer!") + "</h2></div>" +
            "<div class='mb-0'><a href='#'><img src='/static/img/cards/Back.jpg'" +
            "onmouseover=" + '"this.src=' + "'" + card[0] + "'" + '"' +
            "border='0' alt='' height='25%' width='25%'/></a></div>" +
            "<div class='mb-0'><h3>" + _(card[1].capitalize()) + "</h3></div>" +
            "<div class='mb-0'><h4>" + _("Resposta do tarot") + "</h4></div>" +
            "<p class='mb-0'>" + _(chosed_theme) + "</p>" +
            "<div class='mb-0'><h3>" + _("Atenção") + "</h3></div>" +
            "<p class='mb-0'>" + _(card[2]) + "</p>" +
            "</div></div></div></div> " + menu["messages"]
            }


def clairvoyante_sort_cards(name, chosed_card_deck, chosed_theme, menu):

    card_deck = [i+1 for i in range(38)]
    suf(card_deck)
    column = len(name)

    # construire tableau
    def splitBy(li, n=1):
        return [li[i:i+n] for i in range(0, len(li), n)]

    def create_cards_message(card_name, card_img, card_warnings, chosed_theme):
        msg = ["<div class='col'>" +
               "<div class='cta-inner text-center rounded'>" +
               "<a href='#'><img class='card' src='/static/img/cards/Back.jpg'" +
               "onmouseover=" + '"this.src=' + "'" + card_img + "'" + '"' +
               "onmouseout=" + '"this.src=' + "'/static/img/cards/Back.jpg'" + '"' +
               "border='0' alt=''/>" +
               "<span><p>" + _(card_name.capitalize()) + "</p>" +
               "<p>" + _("Atenção") + "</p>" +
               (card_warnings) +
               "<p>" + _("A mensagen da carta!") + "</p>" +
               _(chosed_theme) +
               "</span></a>" +
               "</div></div>"]
        return msg

    def create_final_response(list_of_cards, menu, name, list_of_polarity, chosed_card_deck):

        def polarity_calcul(list_of_polarity):

            items_on_list = len(list_of_polarity)

            def percentage(items_on_list, count_list):
                percentage = count_list * 100/items_on_list
                return percentage

            how_positif = list_of_polarity.count('Positif')
            if how_positif != 0:
                percentage_positif = round(
                    percentage(items_on_list, how_positif), 2)
            else:
                percentage_positif = 0
            how_negatif = list_of_polarity.count('Negatif')
            if how_negatif != 0:
                percentage_negatif = round(
                    percentage(items_on_list, how_negatif), 2)
            else:
                percentage_negatif = 0
            how_neutral = list_of_polarity.count('Neutral')
            if how_neutral != 0:
                percentage_neutral = round(
                    percentage(items_on_list, how_neutral), 2)
            else:
                percentage_neutral = 0

            if percentage_positif == 0 or percentage_negatif == 0 or percentage_neutral == 0:
                if list_of_polarity[0] == "Positif":
                    msg = [_("O resultado é positivo!")]
                if list_of_polarity[0] == "Negatif":
                    msg = [_("O resultado é negativo!")]
                if list_of_polarity[0] == "Neutral":
                    msg = [_("O resultado e revelado pela carta que segue!")]
                return msg[0]

            if percentage_positif > percentage_negatif or percentage_positif > percentage_neutral:
                msg = [
                    _(" O resultado é positivo com ") +
                    str(percentage_positif) + _("% total de cartas a favor!")
                ]
                return msg[0]

            if percentage_negatif > percentage_positif or percentage_negatif > percentage_neutral:
                msg = [
                    _(" O resultado é negativo com ") + str(percentage_negatif) +
                    _("% total de cartas en desfavor, mâs, tudo tem solução o Tarot vai-lhe indicar o caminho...!")
                ]
                return msg[0]
            if percentage_neutral >= percentage_positif or percentage_neutral >= percentage_negatif:
                msg = [
                    _("O resultado revela o equilibrio com ") + str(percentage_neutral) + _("% das cartas!") +
                    _("! Nem muito nem pouco, mas ha sempre aspectos que podem que ser melhorados!")
                ]
                return msg[0]

        def average(chosed_card_deck):
            return sum(chosed_card_deck)/len(chosed_card_deck)

        index_result_card = round(average(chosed_card_deck))
        important_card = response_card(
            name, index_result_card, chosed_theme, menu)
        card_board = splitBy(list_of_cards, column)
        final_card_deck = []
        for i in card_board:
            l = ''.join(i)
            final_card_deck.append(
                "<div class='row' height= '100%' text-align='center'>" + l + "</div>")

        f = ''.join(final_card_deck)

        polarity = polarity_calcul(list_of_polarity)
        print(polarity)

        return {"messages": "<div class='container'>" +
                "<div class='col'><div class='cta-inner text-center rounded'>" +
                "<h4>" + name.capitalize() + _(" aqui esta o resultado das cartas") + "</h4>" +
                "<h4>" + polarity + "</h4>" +
                "<h6>" + _("Para saber os avisos do Tarot passe o rato en cima de cada carta!") + "</h6>" +
                f + "</div></div>" + important_card["messages"]
                }

    if chosed_theme == 'love':

        list_of_cards = []
        list_of_polarity = []
        for i in chosed_card_deck:
            card = get_from_db(i)
            list_of_polarity.append(card[6])
            message_card = create_cards_message(
                card[1], card[0], card[2], card[4])
            list_of_cards.append(message_card[0])

    if chosed_theme == 'work':

        list_of_cards = []
        list_of_polarity = []
        for i in chosed_card_deck:
            card = get_from_db(i)
            list_of_polarity.append(card[6])
            message_card = create_cards_message(
                card[1], card[0], card[2], card[5])
            list_of_cards.append(message_card[0])

    if chosed_theme == 'gen':

        list_of_cards = []
        list_of_polarity = []
        for i in chosed_card_deck:
            card = get_from_db(i)
            list_of_polarity.append(card[6])
            message_card = create_cards_message(
                card[1], card[0], card[2], card[3])
            list_of_cards.append(message_card[0])

    return create_final_response(list_of_cards, menu, name, list_of_polarity, chosed_card_deck)
