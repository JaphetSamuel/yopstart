# Generated by Django 3.0.3 on 2020-03-27 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('youself', '0005_auto_20200322_1705'),
        ('youproj', '0002_auto_20200323_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projet',
            name='porteurs',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='youself.Utilisateur'),
        ),
    ]
