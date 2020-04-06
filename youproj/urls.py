from django.urls import path
from django.views import generic

from . import views

urlpatterns = [
    path('creation/', views.ProjetCreateView.as_view(), name='projet-creation'),
    path('blank/', generic.TemplateView.as_view(template_name='blank.html'), name='blank'),
    path('dashboard/<int:pk>', views.DashboardView.as_view(), name='dashboard'),
    path('fiche/<int:pk>/', views.PresentationView.as_view(), name="projet-presentation"),
    path('liste/', views.listeProjetView.as_view(), name='liste-projet')
]
