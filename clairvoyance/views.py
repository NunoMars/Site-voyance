from django.shortcuts import render
from django.utils.translation import gettext as _
from .logic import clairvoyant
from django.http import Http404, JsonResponse


# Create your views here.

def clairvoyance(request):
    args= {}
    page_title = _("Tirage Tarot")
    args["page_title"]= page_title
    return render(request, 'clairvoyance/index.html', args)


def clairvoyante(request):
    if request.method == 'POST':
        inputs = {}
        asked_items = ['name', 'birth', "number", "right_or_left"]
        input_value = request.POST.get('messageInput', None)        
        i=0
        for i in asked_items:                                          
            inputs[i] = input_value
        result = clairvoyant(inputs['name'], inputs['birth'], inputs['number'], inputs['right_or_left'])
        print(result)
        return JsonResponse(result)
    else:
        raise Http404
