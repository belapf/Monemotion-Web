from django.db import models
from core.models.ano import Ano


class Curso(models.Model):

    SUPERIOR = "Ensino Superior"
    MEDIO = "Ensino Médio"
    POS_GRADUACAO = "Pós Graduação"

    NIVEL_CHOICES = (
        (SUPERIOR, "ensino_superior"),
        (MEDIO, "ensino_medio"),
        (POS_GRADUACAO, "pos_graducao"),
    )

    nome = models.CharField(
        verbose_name='Nome',
        max_length=100,
        blank=True, null=True,
    )

    nivel = models.CharField(
        verbose_name="Nível",
        max_length=20, 
        choices=NIVEL_CHOICES, 
        blank=True, 
        null=True
    )

    ano = models.ForeignKey(
        Ano,
        verbose_name="Ano/Período",
        on_delete=models.SET_NULL,
        blank=True, 
        null=True
    )

    descricao = models.CharField(
        max_length=200 ,
        verbose_name = 'Descricao', 
        blank=True, 
        null=True,

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
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
