from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import gettext as _
from .Ball8 import chose_sentence_ramdomly

# Create your views here.
def ball8(request):
    args= {}
    
    if request.method == "GET":
        
        if request.GET.get('bouton_submit'):
            user_question = request.GET['question']
            args["user_question"] = user_question
            response = chose_sentence_ramdomly
            ball8_message = response
            args["ball8_message"] = ball8_message
    return render(request, 'ball8/ball8.html', args)
