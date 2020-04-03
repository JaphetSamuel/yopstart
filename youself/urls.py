from django.urls import path
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('profile/<int:pk>/', views.UtilisateurDetails.as_view(), name="profile"),
    path('inscription/', views.InscriptionView.as_view(), name='inscription'),
    path('inscription-check/', views.createUser, name="createUser"),
    path('conexion/', views.Connexion.as_view(), name='login'),
    path('deconnexion/', views.DeconnexionView.as_view(),name='deconnexion'),
]