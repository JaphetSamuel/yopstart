# Generated by Django 3.0.3 on 2020-03-21 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youself', '0003_utilisateur_relation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utilisateur',
            name='img_url',
            field=models.ImageField(blank=True, upload_to='profile/', verbose_name='photo de profile'),
        ),
    ]