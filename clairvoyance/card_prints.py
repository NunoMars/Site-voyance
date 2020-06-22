from random import shuffle as suf, choice, randint as rand
from django.utils.translation import gettext as _
from datetime import datetime
from .models import MajorArcana



def one_card(input_value, menu):
    card_deck = [i+1 for i in range(38)]
    suf(card_deck)
    rand_card = choice(card_deck)
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
        "<div class='mb-0'><h2>" + name.capitalize() + _(" o que o tarot tem para lhe dizer!") + "</h2></div>" +        
        "<div class='mb-0'><a href='#'><img src='/static/img/cards/Back.jpg'" +
        "onmouseover=" + '"this.src=' + "'" + card_img + "'" + '"' +
        "border='0' alt='' height='25%' width='25%'/></a></div>" +
        "<div class='mb-0'><h3>" + _(card_name.capitalize()) + "</h3></div>" +          
        "<div class='mb-0'><h4>" + _("Significado en geral") + "</h4></div>" +
        "<p class='mb-0'>" + _(card_signification_gen) + "</p>" +
        "<div class='mb-0'><h3>" + _("Atenção") + "</h3></div>" +
        "<p class='mb-0'>" + _(card_warnings) + "</p>" +
        "<div class='mb-0'><h4>" + _("No amor") + "</h4></div>" +
        "<p class='mb-0'>" + _(card_signification_love) + "</p>" +
        "<div class='mb-0'><h4>" + _("No trabalho") + "</h4></div>" +
        "<p class='mb-0'>" + _(card_signification_work) + "</p>" + 
        "</div></div></div></div> " + menu["messages"]
        }

def clairvoyante_sort_cards(name, cut_point, deck_chosed, chosed_theme, menu):
   
    card_deck = [i+1 for i in range(38)]
    suf(card_deck)
    column = len(name)

    #construire tableau
    def splitBy(li, n=1):
        return [li[i:i+n] for i in range(0, len(li), n)]
    #chisir le tas pour afficher
    if deck_chosed == "left":
        chosen_deck = card_deck[0:cut_point]

    if deck_chosed == "right":
        chosen_deck = card_deck[cut_point:37]
    

    def create_cards_message(card_name, card_img, card_warnings, chosed_theme):
        msg =["<div class='col'>" +
        "<div class='cta-inner text-center rounded'>" +
        "<p class='mb-0'><h4>" + _(card_name.capitalize()) + "</h4></p>" +
        "<p class='mb-0'><a href='#'><img class='card' src='/static/img/cards/Back.jpg'" +
        "onmouseover=" + '"this.src=' + "'" + card_img + "'" + '"' +
        "onmouseout=" + '"this.src=' + "'/static/img/cards/Back.jpg'" + '"' +
        "border='0' alt=''/>" +          
        "<span>" + _(card_warnings) + _(chosed_theme) +
        "</span></a></p>" +                       
        "</div></div>"]
        return msg

    def create_final_response(list_of_cards, menu, name, list_of_polarity, chosen_deck):
        


        def polarity_calcul(list_of_polarity):

            print(list_of_polarity)

            items_on_list = len(list_of_polarity)

            def percentage(items_on_list, count_list):
                percentage = count_list * 100/items_on_list
                return percentage

            how_positif = list_of_polarity.count('Positif')
            if how_positif != 0:
                percentage_positif = round(percentage(items_on_list, how_positif),2)
            else:
                percentage_positif = 0
            how_negatif = list_of_polarity.count('Negatif')
            if how_negatif != 0:
                percentage_negatif = round(percentage(items_on_list, how_negatif),2)
            else:
                percentage_negatif = 0
            how_neutral = list_of_polarity.count('Neutral')
            if how_neutral != 0:
                percentage_neutral = round(percentage(items_on_list, how_neutral),2)
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

            if percentage_positif > percentage_negatif:
                msg = [
                    _(" O resultado é positivo com ") + str(percentage_positif) + _("% de cartas a favor!")
                ]
                return msg[0]
            if percentage_negatif > percentage_positif:
                msg = [
                    _(" O resultado é negativo com ") + str(percentage_negatif) +
                     _("% de cartas en desfavor, mâs, tudo tem solução o Tarot vai-lhe indicar o caminho...!")
                ]
                return msg[0]
            if percentage_neutral > percentage_positif or percentage_neutral > percentage_negatif:
                msg = [
                    _("O resultado revela o equilibrio com ") + str(percentage_neutral) + _("% das cartas!") +
                    _("! Nem muito nem pouco, mas ha sempre aspectos que podem que ser melhorados!")
                ]
                return msg[0]

        
        def average(chosen_deck):
            return sum(chosen_deck)/len(chosen_deck)
        
        index_result_card = round(average(chosen_deck))


        card_board = splitBy(list_of_cards, column)
        final_card_deck = []
        for i in card_board:
            l = ''.join(i)
            final_card_deck.append("<div class='row' height= '100%' text-align='center'>" + l + "</div>")

        f = ''.join(final_card_deck)

        polarity = polarity_calcul(list_of_polarity)

        return {"messages" : "<div class='container'>" +
        "<div class='col'><div class='cta-inner text-center rounded'>" + 
        "<h4>" + name.capitalize() + _(" aqui esta o resultado das cartas") + "</h4>" +
        "<h4>" + polarity + "</h4>" +
        "<h6>" + _("Para saber os avisos do Tarot passe o rato en cima de cada carta!") + "</h6>" +
        f + "</div></div>" + menu["messages"]
        }    
    
    if chosed_theme == 'love':     

        list_of_cards = []
        list_of_polarity = []
        for i in chosen_deck:        
            obj = MajorArcana.objects.get(pk=i)
            card_img = obj.card_image
            card_name = obj.card_name_pt
            chosed_theme = obj.card_signification_love
            card_warnings = obj.card_signification_warnings
            card_polarity = obj.card_polarity
            list_of_polarity.append(card_polarity)
            message_card = create_cards_message(card_name, card_img, card_warnings, chosed_theme)
            list_of_cards.append(message_card[0])

        return create_final_response(list_of_cards, menu, name, list_of_polarity, chosen_deck)

    if chosed_theme == 'work':

        list_of_cards = []
        list_of_polarity = []
        for i in chosen_deck:        
            obj = MajorArcana.objects.get(pk=i)
            card_img = obj.card_image
            card_name = obj.card_name_pt
            chosed_theme = obj.card_signification_work
            card_warnings = obj.card_signification_warnings
            card_polarity = obj.card_polarity
            list_of_polarity.append(card_polarity)
            message_card = create_cards_message(card_name, card_img, card_warnings, chosed_theme)
            list_of_cards.append(message_card[0])


        return create_final_response(list_of_cards, menu, name, list_of_polarity, chosen_deck)
            
    if chosed_theme == 'gen':
        
        list_of_cards = []
        list_of_polarity = []
        for i in chosen_deck:        
            obj = MajorArcana.objects.get(pk=i)
            card_img = obj.card_image
            card_name = obj.card_name_pt
            chosed_theme = obj.card_signification_gen
            card_warnings = obj.card_signification_warnings
            card_polarity = obj.card_polarity
            list_of_polarity.append(card_polarity)
            message_card = create_cards_message(card_name, card_img, card_warnings, chosed_theme)
            list_of_cards.append(message_card[0])


        return create_final_response(list_of_cards, menu, name, list_of_polarity, chosen_deck)
        
