from django.shortcuts import render
from django.utils.translation import gettext as _
from .process import *
from django.http import Http404, JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def clairvoyance(request):
    args= {}
    page_title = _("Tirage Tarot")
    args["page_title"]= page_title
    return render(request, 'clairvoyance/index.html', args)

@csrf_exempt
def clairvoyante(request):
    if request.is_ajax() and request.POST:
        input_value = request.form['messageInput']
        result = grandPyWork(input_value)
        return JsonResponse(result)
    else:
        raise Http404
