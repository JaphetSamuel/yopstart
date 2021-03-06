# Generated by Django 3.0.3 on 2020-04-15 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('youproj', '0007_mediatisation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100)),
                ('details', models.TextField()),
                ('projet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='youproj.Projet')),
            ],
        ),
        migrations.CreateModel(
            name='Tache',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('debut_date', models.DateField(blank=True, verbose_name='Date de debut')),
                ('fin_date', models.DateField(blank=True, verbose_name='Date de fin')),
                ('titre', models.CharField(max_length=100)),
                ('details', models.TextField()),
                ('etat', models.CharField(
                    choices=[('1', 'En attente'), ('2', 'En cour'), ('3', 'Terminée'), ('4', 'Suspendu'),
                             ('0', 'Annulée')], max_length=20)),
                ('activite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='youproj.Activite')),
            ],
        ),
    ]
