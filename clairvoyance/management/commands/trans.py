from django.core.management.base import BaseCommand, CommandError
from google_trans_new import google_translator 
from clairvoyance.models import MajorArcana



class Command(BaseCommand):
    def handle(self, *args, **options):

        trans = google_translator()
        print(trans)

        help = "Insert all products an relations in the models tables."

        print("Debout du travail traduction avec google_traductor!...")

        arcanas = MajorArcana.objects.all()

        print(
            "Nous avons ",
            len(arcanas),
            " a traduire!",
        )

        print("commencement du travail de traduction!")


        try:
            for arcana in arcanas:

                name = arcana.card_name_pt
                warning = arcana.card_signification_warnings_pt
                work = arcana.card_signification_work_pt
                love = arcana.card_signification_love_pt
                gen = arcana.card_signification_gen_pt

                name_fr = trans.translate(name,  lang_tgt='fr')
                name_es = trans.translate( name,  lang_tgt = 'es')
                name_en = trans.translate( name,  lang_tgt = 'en' )

                warning_fr = trans.translate( warning,  lang_tgt = 'fr' )
                warning_es = trans.translate( warning,  lang_tgt = 'es' )
                warning_en = trans.translate( warning,  lang_tgt = 'en' )
                work_fr =  trans.translate( work,  lang_tgt = 'fr' )
                work_es =  trans.translate( work,  lang_tgt = 'es' )
                work_en =  trans.translate( work,  lang_tgt = 'en' )
                love_fr = trans.translate(love, lang_tgt='fr')
                love_es = trans.translate(love, lang_tgt='es')
                love_en = trans.translate(love, lang_tgt='en')
                gen_fr = trans.translate(gen, lang_tgt='fr')
                gen_es = trans.translate(gen, lang_tgt='es')
                gen_en = trans.translate(gen, lang_tgt='en')

                arcana.card_name_fr = name_fr
                arcana.card_name_es = name_es
                arcana.card_name_en = name_en

                
                arcana.card_signification_gen_fr = gen_fr
                arcana.card_signification_gen_es = gen_es
                arcana.card_signification_gen_en = gen_en

                arcana.card_signification_love_fr = love_fr
                arcana.card_signification_love_es = love_es
                arcana.card_signification_love_en = love_en


                arcana.card_signification_work_fr = work_fr
                arcana.card_signification_work_es = work_es
                arcana.card_signification_work_en = work_en


                arcana.card_signification_warnings_fr = warning_fr
                arcana.card_signification_warnings_es = warning_es
                arcana.card_signification_warnings_en = warning_en

                arcana.save()


                print("la traduction de " + arcana.card_name_fr + " c'est bien passé, suivante!")

        except:
            raise CommandError(
                "Ups une erreur est arrivé, insertion aborté!! la carte du tarot",
                arcana.card_name_fr,
            )

        self.stdout.write(
            self.style.SUCCESS(
                "Les cartes sont, à present, traduites et sauvegardées dans la base de données!"
            )
        )

