from django.db import models

from accounts.models import User


class Modalidade(models.Model):
    
    nome = models.CharField(
        verbose_name='Nome',
        max_length=100,
    )

    descricao = models.CharField(
        max_length=200 ,
        verbose_name = 'Descricao', 
        blank=True, null=True,
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
        verbose_name = 'Modalidade'
        verbose_name_plural = 'Modalidades'
