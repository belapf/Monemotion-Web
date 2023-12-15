from django.db import models
from core.models.curso import Curso
from core.models.turno import Turno
from core.models.ano import Ano


class Turma(models.Model):
    # criar atributo nome aqui
        
    descricao = models.CharField(
        verbose_name='Descrição',
        max_length=300, 
        blank=True, null=True,
    )

    curso = models.ForeignKey(
        Curso,
        verbose_name="Curso",
        on_delete=models.SET_NULL,
        blank=True, null=True
    )

    turno = models.ForeignKey(
        Turno,
        verbose_name="Turno",
        on_delete=models.SET_NULL,
        blank=True, null=True
    )

    ano = models.ForeignKey(
        Ano,
        verbose_name="Ano",
        on_delete=models.SET_NULL,
        blank=True, null=True
    )

    data_criacao = models.DateTimeField(
        verbose_name="Data Criação",
        auto_now_add=True
    )

    data_atualizacao = models.DateTimeField(
        verbose_name="Data Atualização",
        auto_now_add=True
    )
    
    def __str__(self):
        '''Método que retorna a representação do objeto como string.'''
        return self.nome

    class Meta:
        '''Sub classe para definir meta atributos da classe principal.'''

        app_label = 'core'
        verbose_name = 'Turma'
        verbose_name_plural = 'Turmas'
