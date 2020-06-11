from django.shortcuts import render
from django.utils.translation import gettext as _
from .process import *
from django.http import Http404, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect

# Create your views here
def clairvoyance(request):
    args= {}
    page_title = _("Tirage Tarot")
    args["page_title"]= page_title
    return render(request, 'clairvoyance/index.html', args)


def clairvoyante(request):
    if request.is_ajax():
        input_value = request.GET['messageInput']
        """print(input_value)"""
        result = input_value
        return JsonResponse(result)
    else:
        raise Http404
