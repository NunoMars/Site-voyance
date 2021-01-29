from django.shortcuts import render
from django.utils.translation import gettext as _
from .logic import clairvoyant
from django.http import Http404, JsonResponse


def index(request):
    args= {
        "page_title" : _("Mundo Do Tarot"),
        "first_title" : _("Benvindo ao Meu mundo"),
        "second_title" : _("TAROT T"),
        }

    return render(request, 'clairvoyance/home.html', args)

def clairvoyance(request):
    args = {}
    page_title = _("Tarot")
<<<<<<< HEAD
    args["page_title"]= page_title
    return render(request, 'clairvoyance/clairvoyante.html', args)
=======
    args["page_title"] = page_title
    return render(request, 'clairvoyance/index.html', args)
>>>>>>> 562998888abf2d57cf0376d228dbbd7f91f634f5


def clairvoyante(request):
    if request.method == 'POST':
        try:
            input_value = request.POST.get('messageInput')
            result = clairvoyant(input_value)
            return JsonResponse(result)
        except ValueError:
            pass
    else:
<<<<<<< HEAD
        pass 


def history(request):
    pass
=======
        pass
>>>>>>> 562998888abf2d57cf0376d228dbbd7f91f634f5
