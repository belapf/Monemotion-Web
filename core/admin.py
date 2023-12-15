from django.contrib import admin
from core.models.ano import Ano
from core.models.curso import Curso
from core.models.modalidade import Modalidade

from core.models.turma import Turma
from core.models.turno import Turno


@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'descricao',
    ]

    fields = (
        'descricao', 
        'curso',
        'turno',
    )  
    
@admin.register(Turno)
class TurnoAdmin(admin.ModelAdmin):
     list_display= [
         'nome',
     ]
     fields = (
        'nome', 
        )  


@admin.register(Modalidade)
class ModalidadeAdmin(admin.ModelAdmin):
     list_display= [
         'nome',
     ]
     fields = (
        'nome', 
        'descricao'
        )  
@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
     list_display= [
         'nome',
     ]
     fields = (
        'nome', 
        'descricao'
        )  
    

@admin.register(Ano)
class AnoAdmin(admin.ModelAdmin):
     list_display= [
         'nome',
     ]
     fields = (
        'nome', 
        )  