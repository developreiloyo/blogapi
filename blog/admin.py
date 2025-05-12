from django.contrib import admin
from .models import *

class CategoriaAdmin(admin.ModelAdmin):
    search_fields =['nombre']
    list_display = ('id','nombre','fecha_creacion','estado',)

class AutorAdmin(admin.ModelAdmin):
    search_fields =['nombres', 'apellidos', 'correo','id']
    list_display = ('nombre', 'apellidos', 'email', 'estado','id')

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Post)
