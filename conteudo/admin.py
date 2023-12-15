from django.contrib import admin
from conteudo.models.categoria import Categoria

from conteudo.models.conteudo import Conteudo

@admin.register(Conteudo)
class ConteudoAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'titulo',
    ]
    
    readonly_fields = ('data_criacao', 'data_atualizacao', 'usuario_criacao','usuario_atualizacao')

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
     list_display= [
         'id',
         'titulo',
         'descricao',
     ]
     readonly_fields = ('data_criacao', 'data_atualizacao')

# Register your models here.
