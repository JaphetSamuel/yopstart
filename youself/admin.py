from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Utilisateur)
class UtilisateurAdmin(admin.ModelAdmin):
    pass


@admin.register(Competence)
class CompetenceAdmin(admin.ModelAdmin):
    pass


@admin.register(Domaine)
class DomaineAdmin(admin.ModelAdmin):
    pass