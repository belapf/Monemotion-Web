from django.db import models
class Categoria(models.Model):
    
    NOTICIA = 'Noticia'
    VIDEO = 'Video'
    PODCAST = 'Podcast'
    OUTROS = 'outros'

    TAG_CHOICES = (
        (NOTICIA, 'Noticia'),
        (VIDEO, 'Video'), 
        (PODCAST, 'Podcast'),
        (OUTROS, 'outros'),  
    )

    
    titulo = models.CharField(
        max_length=100 ,
        verbose_name = 'Titulo', 
    )
    

    descricao = models.CharField(
        max_length=200 ,
        verbose_name = 'Descricao', 
    ) 

    tag = models.CharField(
        max_length=50,
        choices=TAG_CHOICES,
        blank=True,
        null=True
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
        return "{}".format(self.titulo)
    
    class Meta:
        app_label = 'conteudo'
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias' 
