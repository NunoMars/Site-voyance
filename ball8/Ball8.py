from random import shuffle as suf, choice as ch
from .models import Sentences

#start program
continuer_partie = True 
print("BIENVENNU Sur l'Oracle")
print("Concentrez-vous sur la question à poser")


def chose_sentence_ramdomly():
	obj = Sentences.objects.all()
	response = ch(obj)
	response = response.sentence
	return response

	
	user_question = input("Quelle est la question que vous voulez poser?")

	user_answer = input("Dées que vous êtes prêt, a inerroger la balle, appuyez sur 'ENTREE'")

	print("A la question : ",user_question, "la réponse est : ",get_random_item_in(chose_list(master_list)))
	
