from youself.models import *
from youproj.models import *

def calla(ctxt):
    return {
        'list_domaines' : Domaine.objects.all(),
        'list_competences' : Competence.objects.all(),
        'list_utilis': Utilisateur.objects.all(),
        'list_projets': Projet.objects.all(),
    }
