from django.shortcuts import render
from django.utils.translation import gettext as _
from .logic import clairvoyant
from django.http import Http404, JsonResponse


def index(request):
    args= {}
    page_title = _("Mundo Do Tarot")
    args["page_title"] = page_title
    first_title = _("Benvindo ao Meu mundo")
    args["first_title"] = first_title
    second_title = _("TAROT T")
    args["second_title"] = second_title
    return render(request, 'clairvoyance/home.html', args)

def clairvoyance(request):
    args= {}
    page_title = _("Tarot")
    args["page_title"]= page_title
    return render(request, 'clairvoyance/clairvoyante.html', args)


def clairvoyante(request):
    if request.method == 'POST':    
        try:
            input_value = request.POST.get('messageInput')
            result = clairvoyant(input_value)
            return JsonResponse(result)
        except ValueError:
            pass
    else:
        pass 


def history(request):
    pass