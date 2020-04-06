from django.http import QueryDict
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


class listeProjetView(generic.ListView):
    model = Projet
    queryset = Projet.objects.all()
    template_name = 'youproj/liste.html'
    paginate_by = 10

    # def get(self, request, *args, **kwargs):
    #     if self.request.GET['domaine'] and self.request.GET['domaine'] != '':
    #         self.queryset= Projet.objects.filter(domaine__label__contains=self.request.GET['domaine'])

    #     return super().get(request, **kwargs)

    def trystry(self, tab: list) -> list:
        res: list = list()
        for x in tab:
            try:
                res.append(int(x))
            except:
                pass
        return res

    def get_queryset(self):
        query = Projet.objects.all()
        params: QueryDict = self.request.GET
        try:
            if self.request.GET.get('tags', None) is not None:
                print(self.request.GET.keys())
                doms = self.trystry(self.request.GET.keys())
                if doms.__len__() >= 1:
                    self.extra_context = {'selected_doms': doms}
                    self.queryset = Projet.objects.filter(domaine_id__in=doms)
                if self.request.GET.get('tags', None) is not None:
                    self.queryset.filter(tags__contains=self.request.GET['tags'])
        except Exception as e:
            print(e.__dict__)
        return self.queryset
