from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpRequest
from django.forms import TextInput, PasswordInput, EmailInput
from .models import *

# Create y
# our views here.

class index(generic.base.TemplateView):
    template_name = 'index.html'


class UtilisateurDetails(generic.DetailView):
    model = Utilisateur
    template_name = 'youself/u_details.html'


class CustomUserCreationform(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)
        widgets = {
            'username': TextInput(attrs={'class':'form-control mb-4', 'placeholder':"nom d'utilisateur"}),
            'email': EmailInput(attrs={'class':'form-control mb-4', 'placeholder':"email"}),
            'new-password1': PasswordInput(attrs={'class':'form-control mb-4'}),
            'password2': PasswordInput(attrs={'class':'form-control mb-4'})
        }
        help_texts = {
            'username':"Caractère alphanumeirique",
            'password1':'',
        }


class InscriptionView(generic.TemplateView):
    list_competences = Competence.objects.all()
    domaines = Domaine.objects.all()
    ctuf = CustomUserCreationform()
    template_name = 'account/inscription.html'

    def get_context_data(self, **kwargs):
        contexte = super().get_context_data(**kwargs)
        customdict = {
        'list_competences':self.list_competences,
        'domaines':self.domaines,
        'creation_form': CustomUserCreationform(),
        **contexte
        }

        return customdict

class Connexion(LoginView):
    template_name = 'account/connexion.html'



def createUser(request):
    username = request.POST['username']
    prename = request.POST['prename']
    email = request.POST['email']
    name = request.POST['name']
    mdp = request.POST['pass']
    msg = f"username {username}, nom {name}, prenom {prename}, mot de passe {mdp}"

    if username != '' and prename != '' and name != '' and mdp != '' and email != '':
        u = User(username=username, first_name=prename, last_name=name, email=email)
        u.set_password(mdp)
        u.save()
        ut = Utilisateur(user=u)
        ut.save()
        login(request,u)

    return redirect('profile', pk=ut.id)

class DeconnexionView(generic.RedirectView):
    pattern_name = 'home'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, **kwargs)

def home(request):
    contexte = {
        'domaine' : Domaine.objects.all(),
        'Competence' : Competence.objects.all()
    }

    devs = Utilisateur.objects.all()
    # if request.GET['domaine'] and request.GET['domaine'] != '':
    #     devs = Utilisateur.objects.get(domaine = request.GET['domaine'])
    # if request.GET['competence'] and request.GET['competence'] != '' :
    #     devs = Utilisateur.objects.get(competences = request.GET['competence'])

    #contexte['devs'] = devs

    return render(request, template_name='home.html', context=contexte)