# Generated by Django 3.0.3 on 2020-05-31 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MajorArcana',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_name_pt', models.CharField(max_length=50)),
                ('card_signification_gen', models.TextField()),
                ('card_signification_warnings', models.TextField()),
                ('card_signification_love', models.TextField()),
                ('card_signification_work', models.TextField()),
                ('card_image', models.CharField(max_length=100)),
            ],
        ),
    ]