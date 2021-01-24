from django.urls import path
from .views import GalleryView

urlpatterns = [
    path('galeria', GalleryView.as_view(), name='gallery')
]
