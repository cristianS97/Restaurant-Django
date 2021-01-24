from django.db import models

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=15, verbose_name='Nombre categoría')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Última actualización')
    def __str__(self):
        return self.category

class Food(models.Model):
    name = models.CharField(max_length=30, verbose_name='Platillo')
    category_id = models.ForeignKey(Category, verbose_name='Categoria', on_delete=models.CASCADE)
    price = models.IntegerField(verbose_name='Precio $', default=0)
    image = models.ImageField(verbose_name='Imagen', upload_to='static/img', default=None)
    in_index = models.BooleanField(verbose_name='Muestra en inicio', default=False)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Última actualización')

