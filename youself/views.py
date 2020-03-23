from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.forms import TextInput, PasswordInput, EmailInput
from .models import *

# Create y
# our views here.

def index(request):
    return render(request, template_name="index.html")


class UtilisateurDetails(DetailView):
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


def InscriptionView(request):
    list_competences = Competence.objects.all()
    domaines = Domaine.objects.all()
    ctuf = CustomUserCreationform()
    contexte = {
        'list_competences':list_competences,
        'domaines':domaines,
        'creation_form': CustomUserCreationform()
    }

    return render(request,'account/inscription.html',contexte)

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

    return redirect('profile',pk=ut.id)


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