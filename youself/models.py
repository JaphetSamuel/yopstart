from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Competence(models.Model):
    label = models.CharField(max_length=100)

    def __str__(self):
        return self.label


class Domaine(models.Model):
    label = models.CharField(max_length=100)

    def __str__(self):
        return  self.label

class Utilisateur(models.Model):
    relation = models.ManyToManyField('Utilisateur', blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, limit_choices_to={'is_superuser':False})
    date_naissance = models.DateField(blank=True)
    bio = models.TextField()
    pays = models.CharField(max_length=50, blank=True)
    competences = models.ManyToManyField(Competence,blank=True)
    domaine = models.ManyToManyField(Domaine, blank=True)
    img_url = models.ImageField(verbose_name='photo de profile', blank=True, upload_to='profile/')

    def __str__(self):
        return self.user.username

    def patronyme(self):
        return f"{self.user.first_name} {self.user.last_name}"