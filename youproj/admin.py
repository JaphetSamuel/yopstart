from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(Projet)
class ProjetAdmin(admin.ModelAdmin):
    pass


@admin.register(Mediatisation)
class MediatisationAdmin(admin.ModelAdmin):
    pass


@admin.register(Finance)
class FinanceAdmin(admin.ModelAdmin):
    pass


@admin.register(Stats)
class StatsAdmin(admin.ModelAdmin):
    pass


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    pass
