from django.shortcuts import render
from django.views.generic import DetailView
from django.views.decorators.http import require_http_methods
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
    contexte = {
        'list_competences':list_competences,
        'domaines':domaines,
        'creation_form': CustomUserCreationform()
    }
    return render(request,'account/inscription.html',contexte)
