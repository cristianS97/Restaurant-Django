from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
class HomeView(TemplateView):
    template_name = 'index.html'
    # Procesamos la respuesta de la vista
    def get(self, request, *args, **kwargs):
        context = {
            'titulo': 'Inicio',
            'imagenes': list(range(6))
        }
        return render(request, self.template_name, context)