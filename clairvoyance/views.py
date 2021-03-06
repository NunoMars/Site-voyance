from django.shortcuts import render, redirect
from django.utils.translation import gettext as _
from .logic import clairvoyant
from django.http import Http404, JsonResponse
from django.contrib.auth.decorators import login_required
from .models import MajorArcana
from accounts.models import CustomUser, History, DailySortedCards
from django.contrib.auth.models import User
import datetime


def index(request):
    args= {
        "first_title" : _("Benvindo ao Meu mundo"),
        "second_title" : _("TAROT T"),
        }

    return render(request, 'home.html', args)


def clairvoyance(request):
    args = {}
    page_title = _("Tarot")
    args["page_title"]= page_title
    
    return render(request, 'clairvoyance/clairvoyance.html', args)

def card_deck(request):
    language= request.LANGUAGE_CODE
    args = {}
    cards = MajorArcana.objects.all()
    args["cards"] = cards
    args["language"] = language
    return render(request, 'clairvoyance/card_deck.html', args)

def card_detail(request, card):
    language= request.LANGUAGE_CODE
    args = {}
    card = MajorArcana.objects.get(id=card.id)
    args["card"] = card
    args["language"] = language
    return render(request, 'clairvoyance/card_detail.html', args)

def clairvoyante(request):
    language= request.LANGUAGE_CODE
    if request.method == 'POST':
        try:
            input_value = request.POST.get('messageInput')
            result = clairvoyant(input_value, language)

            if input_value == "rec":

                if request.user.is_authenticated:                   

                    user = request.user
                    sorted_card=result[0]
                    chosed_theme=result[1]
                    date = datetime.datetime.today()
                    
                    try:
                        h = History.objects.create(
                        user=user,
                        sorted_card=sorted_card,
                        chosed_theme=chosed_theme,
                        sorted_cards_date=date  
                        )
                        h.save()
                        return JsonResponse(result[2])

                    except:
                        return JsonResponse(
                            {
                                'messages': "<h3>" + _("Impossible d'enregistrer le tirage, rafraîchissez la page svp!") + "</h3>"
                            }
                        )
                        
                else:
                    return JsonResponse(
                        {
                            'messages':"<div class='container-fluid w-100 h-100'> "+
                            "<div class='row h-100 w-100 justify-content-center align-items-center text-cente'>" +
                            "<div class='col align-items-center text-center' >" +
                            '<a href="{% url ' + "'history'" + ' %}">LOGIN</a>'
                        }
                    )
            
            else:
                return JsonResponse(result)
            
        except ValueError:
            pass
    else:
        pass 

@login_required()
def user_history(request):
    """Fonction for show the sorted cards,
     login required."""
    user = request.user
    user = CustomUser.objects.get(email=user)

    user_history = History.objects.filter(user=user)
    daily_user_card = DailySortedCards.objects.filter(user=user)
    """products_list = []
    for item in get_user_history:
        chosen_product = item.chosen_product
        products_list.append(chosen_product)
        remplacement_product = item.remplacement_product
        products_list.append(remplacement_product)"""

    context = {
        "user": user,
        "user_history": user_history,
        "daily_user_card": daily_user_card
    }
    return render(request, "clairvoyance/history.html", context)

def contacts(request):
    return render(request, 'clairvoyance/contacts.html')

