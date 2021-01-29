from django.urls import path
from . import views

urlpatterns = [
    path('contacto', views.ContactView.as_view(), name='contact'),
    path('check', views.CheckView.as_view(), name='check'),
    path('cierre', views.logout, name='logout'),
]