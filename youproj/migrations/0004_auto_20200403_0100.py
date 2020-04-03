# Generated by Django 3.0.3 on 2020-04-03 00:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('youproj', '0003_auto_20200327_1212'),
    ]

    operations = [
        migrations.AddField(
            model_name='projet',
            name='date_debut',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='projet',
            name='img_url',
            field=models.ImageField(blank=True, default='youproj/illustration.png', upload_to='youproj/'),
        ),
        migrations.AddField(
            model_name='projet',
            name='somme_besoin_actuelle',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]