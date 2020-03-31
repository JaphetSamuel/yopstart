from django.db import models
from youself.models import *

# Create your models here.

class Projet(models.Model):
    etats = (
        ("0","non precisé"),
        ("1","idée"),
        ("2","rédaction de plan"),
        ("3","prototype"),
        ("4","phase de test"),
        ("4","phase de commercialisation"),
    )

    nom = models.CharField(max_length=100)
    porteurs = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, blank=True)
    equipe = models.ManyToManyField(Utilisateur, blank=True),
    domaine = models.ForeignKey(Domaine, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    date_debut= models.DateField(blank=True),
    avancement = models.TextField(blank=True)
    lien_depot = models.URLField( blank=True)
    phase = models.CharField(max_length=100, choices=etats, default='-')

    def __str__(self):
        return self.nom
