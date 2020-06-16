from django.shortcuts import render
from django.utils.translation import gettext as _
from .logic import clairvoyant
from django.http import Http404, JsonResponse


# Create your views here.

def clairvoyance(request):
    args= {}
    page_title = _("Tarot")
    args["page_title"]= page_title
    return render(request, 'clairvoyance/index.html', args)


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