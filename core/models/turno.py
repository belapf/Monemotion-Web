from django.db import models


class Turno(models.Model):
    
    nome = models.CharField(
        verbose_name='Nome',
        max_length=100,
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
        verbose_name = 'Turno'
        verbose_name_plural = 'Turnos'
