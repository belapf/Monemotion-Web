from django.db import models


class Ano(models.Model):
    
    nome = models.CharField(
        verbose_name='Nome',
        max_length=100,
    )

    def __str__(self):
        '''Método que retorna a representação do objeto como string.'''
        return self.nome

    class Meta:
        '''Sub classe para definir meta atributos da classe principal.'''

        app_label = 'core'
        verbose_name = 'Ano/Período'
        verbose_name_plural = 'Ano/Período'
