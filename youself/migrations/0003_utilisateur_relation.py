# Generated by Django 3.0.3 on 2020-03-18 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youself', '0002_auto_20200318_1509'),
    ]

    operations = [
        migrations.AddField(
            model_name='utilisateur',
            name='relation',
            field=models.ManyToManyField(blank=True, to='youself.Utilisateur'),
        ),
    ]
