from django.contrib import admin
from .models import Category, Food
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    # Indicamos los campos que serán de solo lectura
    readonly_fields = ('created', 'updated')
    ordering = ['pk']
    list_display = ('pk', 'category', 'created', 'updated')

class FoodAdmin(admin.ModelAdmin):
    # Indicamos los campos que serán de solo lectura
    readonly_fields = ('created', 'updated')
    ordering = ('created', 'updated')
    list_display = ('name', 'get_category', 'created', 'updated')
    list_filter = ('category_id', )
    
    def get_category(self, obj):
        return obj.category_id.category

admin.site.register(Category, CategoryAdmin)
admin.site.register(Food, FoodAdmin)