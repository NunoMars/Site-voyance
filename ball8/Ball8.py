from random import shuffle as suf, choice as ch
from .models import Sentences


print("BIENVENNU Sur l'Oracle")
print("Concentrez-vous sur la question à poser")


def chose_sentence_ramdomly():
    obj = Sentences.objects.all()
    response = ch(obj)
    response = response.sentence
    return response
