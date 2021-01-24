from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Category, Food

# Create your views here.
class GalleryView(TemplateView):
    template_name='galeria.html'
    categorias = Category.objects.all()
    title = 'Galeria de imagenes'

    def get(self, request, *args, **kwargs):
        context = {
            'titulo': self.title,
            'categorias': self.categorias,
            'platos': Food.objects.filter(category_id=int(self.categorias[0].pk))
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        my_selection = int(request.POST['menu-categoria'])
        context = {
            'titulo': self.title,
            'seleccion': my_selection,
            'categorias': self.categorias,
            'platos': Food.objects.filter(category_id=my_selection)
        }
        return render(request, self.template_name, context)
