# Generated by Django 3.1.5 on 2021-02-12 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210208_1827'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='user_language',
            field=models.CharField(default='fr', max_length=20),
        ),
    ]
