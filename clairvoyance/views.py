from django.shortcuts import render
from django.utils.translation import gettext as _
from .logic import clairvoyant
from django.http import Http404, JsonResponse
from django.contrib.auth.decorators import login_required
from accounts.models import CustomUser, History
from django.contrib.auth.models import User


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


def clairvoyante(request):
    language= request.LANGUAGE_CODE
    if request.method == 'POST':
        try:
            input_value = request.POST.get('messageInput')

            result = clairvoyant(input_value, language)

            return JsonResponse(result)
        except ValueError:
            pass
    else:
        pass 

@login_required
def history(request):
    """Show the sorted card history,
    tha are chosed by the user, login required."""
    user = request.user
    user = CustomUser.objects.get(email=user)

    user_history = History.objects.filter(user=user)

    context = {
        "user": user
    }

    return render(request, "products/history.html", context)

def contacts(request):
    return render(request, 'clairvoyance/contacts.html')

def csrf_failure(request):
    args = {'csrf_failure' : _("Ups temos un pequenino problema com o Csrf... recarrege a pàgina por favor!")}
    return render(request, '500.html', args)
