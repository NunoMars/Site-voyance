# Generated by Django 3.0.7 on 2020-06-29 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sentences',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sentence', models.CharField(max_length=200)),
                ('sentence_polarity', models.CharField(choices=[('Positif', 'Positif'), ('Negatif', 'Negatif'), ('Neutral', 'neutral')], default='Positif', max_length=10)),
            ],
        ),
    ]