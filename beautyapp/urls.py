from django.urls import path
from beautyapp import views

urlpatterns = [
    path('', views.home, name = 'home'),
]
