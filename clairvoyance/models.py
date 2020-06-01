from django.db import models

# Create your models here.
class MajorArcana(models.Model):
    """ Class to define the mayor cards deck."""
    card_name_pt = models.CharField(max_length=50)
    card_signification_gen = models.TextField()
    card_signification_warnings = models.TextField()
    card_signification_love = models.TextField()
    card_signification_work = models.TextField()
    card_image = models.CharField(max_length=100)
