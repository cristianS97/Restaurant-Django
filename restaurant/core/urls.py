from django.urls import path
from . import views

urlpatterns = [
    path('cerrar_sesion', views.logout, name='logout')
]
