from django.core.management.base import BaseCommand, CommandError
from google_trans_new import google_translator 
from ball8.models import Sentences



class Command(BaseCommand):
    def handle(self, *args, **options):

        trans = google_translator()


        help = "Insert all products an relations in the models tables."

        print("Debout du travail traduction avec google_traductor!...")

        sentences = Sentences.objects.all()

        print(
            "Nous avons ",
            len(sentences),
            "phrases a traduire!",
        )

        print("commencement du travail de traduction!")


        try:
            for sentence in sentences:             

                sentence_pt = sentence.sentence
                print(sentence_pt)

                sentence_fr = trans.translate(sentence_pt,  lang_tgt='fr')
                print(sentence_fr)
                sentence.sentence_fr = sentence_fr

                sentence_es = trans.translate(sentence_pt,  lang_tgt = 'es')
                print(sentence_es)
                sentence.sentence_es = sentence_es

                sentence_en = trans.translate(sentence_pt,  lang_tgt = 'en')
                print(sentence_en)
                sentence.sentence_en = sentence_en

                sentence.save()               
                
                print("la traduction de " + sentence + " c'est bien passé, suivante!")

        except:
            raise CommandError(
                "Ups une erreur est arrivé, insertion aborté!!",
                sentence_fr,
            )

        self.stdout.write(
            self.style.SUCCESS(
                "Les phrases sont, à present, traduites et sauvegardées dans la base de données!"
            )
        )