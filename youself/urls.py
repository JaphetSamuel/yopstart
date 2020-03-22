from django.urls import path
from . import views
from django.views.generic.base import TemplateResponse

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/<int:pk>/', views.UtilisateurDetails.as_view(), name="profile"),
    path('inscription/', views.InscriptionView, name='inscription'),
    path('inscription-check/', views.createUser, name="createUser"),
]