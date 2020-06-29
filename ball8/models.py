from django.db import models

# Create your models here.
class Sentences(models.Model):
    """ Class to define the response sentences."""
    CHOICES = (
        ("Positif", "Positif"),
        ("Negatif", "Negatif"),
        ("Neutral", "neutral") 
    )
    sentence = models.CharField(max_length=200)
    sentence_polarity = models.CharField(max_length=10, choices=CHOICES, default="Positif")