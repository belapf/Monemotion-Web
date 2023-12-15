from django.contrib import admin

from .models.emocao import Emocao

# Register your models here.
@admin.register(Emocao)
class EmocaoAdmin(admin.ModelAdmin):
    list_display = [
        'motivo', 
        'descricao' 
    ]


    #readonly_fields = ('motivo','data_criacao', 'data_atualizacao', 'usuario_criacao','usuario_atualizacao')
