from django.shortcuts import render
from .models import *
from django.views import generic
from django.contrib.auth import mixins
from youself.models import Utilisateur


# Create your views here.

class ProjetCreateView(mixins.LoginRequiredMixin, generic.edit.CreateView):
    model = Projet
    fields = ['nom', 'domaine', 'description', 'avancement', 'phase', 'lien_depot']
    template_name = 'youproj/create.html'

    def form_valid(self, form):
        form.instance.porteurs = self.request.user.utilisateur
        form.instance.porteurs_id = self.request.user.utilisateur.id
        return super().form_valid(form)

    def get_success_url(self):
        return f"/projet/dashboard/{self.object.id}"


class DashboardView(generic.DetailView):
    model = Projet
    template_name = 'youproj/dashbord.html'
    context_object_name = 'projet'


class PresentationView(generic.DetailView):
    model = Projet
    template_name = 'youproj/presentation.html'
