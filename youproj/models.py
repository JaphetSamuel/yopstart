import time
from datetime import date

from django.db import models
from youself.models import *


# Create your models here.

class Projet(models.Model):
    etats = (
        ("0", "non precisé"),
        ("1", "idée"),
        ("2","rédaction de plan"),
        ("3","prototype"),
        ("4","phase de test"),
        ("4","phase de commercialisation"),
    )

    nom = models.CharField(max_length=100)
    img_url = models.ImageField(upload_to='youproj/', blank=True, default='youproj/illustration.png')
    porteurs = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, blank=True)
    equipe = models.ManyToManyField(Utilisateur, blank=True),
    domaine = models.ForeignKey(Domaine, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    date_debut = models.DateField(blank=True, default=date.today)
    avancement = models.TextField(blank=True)
    somme_besoin_actuelle = models.IntegerField(blank=True, default=0)
    lien_depot = models.URLField(blank=True)
    phase = models.CharField(max_length=100, choices=etats, default='-')
    tags = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.nom
