# Generated by Django 3.0.3 on 2020-04-03 11:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('youproj', '0004_auto_20200403_0100'),
    ]

    operations = [
        migrations.AddField(
            model_name='projet',
            name='tags',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]