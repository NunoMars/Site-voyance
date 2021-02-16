from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class MajorArcana(models.Model):
    """ Class to define the mayor cards deck."""
    CHOICES = (
        ("Positif", "Positif"),
        ("Negatif", "Negatif"),
        ("Neutral", "neutral")
    )

    card_name_pt = models.CharField(max_length=50)
    card_name_fr = models.CharField(max_length=50, default="Arcane")
    card_name_es = models.CharField(max_length=50, default="Arcane")
    card_name_en = models.CharField(max_length=50, default="Arcane")
    card_signification_gen_pt = models.TextField()
    card_signification_gen_fr = models.TextField(default='gen')
    card_signification_gen_es = models.TextField(default='gen')
    card_signification_gen_en = models.TextField(default='gen')
    card_signification_warnings_pt = models.TextField()
    card_signification_warnings_fr = models.TextField(default="warning")
    card_signification_warnings_es = models.TextField(default="warning")
    card_signification_warnings_en = models.TextField(default="warning")
    card_signification_love_pt = models.TextField()
    card_signification_love_fr = models.TextField(default='love')
    card_signification_love_es = models.TextField(default='love')
    card_signification_love_en = models.TextField(default='love')
    card_signification_work_pt = models.TextField()
    card_signification_work_fr = models.TextField(default='work')
    card_signification_work_es = models.TextField(default='work')
    card_signification_work_en = models.TextField(default='work')
    card_image = models.CharField(max_length=100)
    card_polarity = models.CharField(
        max_length=10, choices=CHOICES, default="Positif")
