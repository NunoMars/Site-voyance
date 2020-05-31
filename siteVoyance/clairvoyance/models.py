from django.db import models

# Create your models here.
class MajorArcana(models.Model):
    """ Class to define the mayor cards deck."""
    card_name_fr = models.CharField(max_length=50)
    card_signification_fr = models.TextField()
    card_image = models.URLField()
