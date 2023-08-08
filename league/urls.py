from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='base'),
    path('players/', views.index, name='team-details'),
    path('statistics/', views.stat, name='players-stat'), 
    path('', views.register, name='register'),
    path('login/', views.log, name='login'),
     path('logout/', views.out, name='logout')
]