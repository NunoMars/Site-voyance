# Generated by Django 3.0.7 on 2020-06-20 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clairvoyance', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='majorarcana',
            name='card_palarity',
            field=models.CharField(choices=[('Positif', 'Positif'), ('Negatif', 'Negatif')], default='Positif', max_length=10),
        ),
    ]
