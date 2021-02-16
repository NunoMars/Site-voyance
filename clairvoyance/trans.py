from googletrans import Translator
from clairvoyance.models import MajorArcana


trad = Translator()

arcanas = MajorArcana.objects.all()


for arcana in arcanas:
    name = arcana.card_name_pt
    warning = arcana.card_signification_warnings_pt
    work = arcana.card_signification_work_pt
    love = arcana.card_signification_love_pt
    gen = arcana.card_signification_gen_pt

    name_fr = trad.translate( name,  dest = 'fr' )
    warning_fr = trad.translate( warning,  dest = 'fr' )
    work_fr =  trad.translate( warning,  dest = 'fr' )
    love_fr = trad.translate(love, dest='fr')
    gen_fr = trad.translate(gen, dest='fr')

    arcana.card_name_fr = name_fr
    arcana.card_signification_gen_fr = gen_fr
    arcana.card_signification_love_fr = love_fr
    arcana.card_signification_work_fr = work_fr
    arcana.card_signification_warnings_fr = warning_fr
    arcana.save()