import os
import time
from datetime import date

from django.db import models
from youself.models import *


# Create your models here.

class Role(models.Model):
    role = models.CharField(max_length=100)
    personne = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.personne}, {self.role}"


class Stats(models.Model):
    suiveurs = models.ManyToManyField(Utilisateur, related_name="projet_suivi")
    etoile = models.IntegerField()
    projet = models.OneToOneField('Projet', on_delete=models.CASCADE)

    def __str__(self):
        return f'stats du projet {self.projet.nom}'


class Finance(models.Model):
    somme_investi = models.IntegerField()
    somme_requise = models.IntegerField()
    somme_depense = models.IntegerField()
    projet = models.OneToOneField('Projet', on_delete=models.CASCADE)

    releve_url = 'url'

    def somme_restante(self):
        return self.somme_investi - self.somme_depense


class Projet(models.Model):
    etats = (
        ("0", "non precisé"),
        ("1", "idée"),
        ("2", "rédaction de plan"),
        ("3", "prototype"),
        ("4", "phase de test"),
        ("4", "phase de commercialisation"),
    )

    nom = models.CharField(max_length=100)
    img_url = models.ImageField(upload_to='youproj/', blank=True, default='youproj/illustration.png')
    porteurs = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, blank=True)
    equipe = models.ManyToManyField(Role, blank=True)
    domaine = models.ForeignKey(Domaine, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    date_debut = models.DateField(blank=True, default=date.today)
    avancement = models.TextField(blank=True)
    lien_depot = models.URLField(blank=True)
    phase = models.CharField(max_length=100, choices=etats, default='-')
    tags = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.nom
