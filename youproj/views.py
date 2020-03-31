from django.shortcuts import render
from .models import *
from django.views.generic.edit import CreateView
from django.contrib.auth import mixins
from youself.models import Utilisateur


# Create your views here.

class ProjetCreateView(mixins.LoginRequiredMixin, CreateView):
    model = Projet
    fields = ['nom', 'domaine', 'description', 'avancement', 'phase', 'lien_depot']
    template_name = 'youproj/create.html'

    def form_valid(self, form):
        form.instance.porteurs = self.request.user.utilisateur
        form.instance.porteurs_id = self.request.user.utilisateur.id
        self.success_url = f'/profile/{self.request.user.utilisateur.id}'
        return super().form_valid(form)
