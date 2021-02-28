from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import gettext as _
from random import shuffle as suf, choice as ch
from .models import Sentences


def ball8(request):
    args = {}
    language= request.LANGUAGE_CODE

    if request.method == "GET":

        if request.GET.get('bouton_submit'):
            user_question = request.GET['question']
            page_title = _("ORÁCULO")
            args["page_title"] = page_title
            args["user_question"] = user_question

            sentences = Sentences.objects.all()
            rand_message = ch(sentences)
            
            if language == 'pt':
                ball8_message = rand_message.sentence
                args["ball8_message"] = ball8_message

            if language == 'es':
                ball8_message = rand_message.sentence_es
                args["ball8_message"] = ball8_message

            if language == 'en':
                ball8_message = rand_message.sentence_en
                args["ball8_message"] = ball8_message
                
            else:
                ball8_message = rand_message.sentence_fr
                args["ball8_message"] = ball8_message

            
    return render(request, 'ball8/ball8.html', args)
