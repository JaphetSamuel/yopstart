from django.urls import path
from . import views

urlpatterns = [
    path('creation/', views.ProjetCreateView.as_view(), name='projet-creation'),
]
