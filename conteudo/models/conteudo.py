from django.db import models
from accounts.models import User
from conteudo.models.categoria import Categoria

class Conteudo(models.Model):

    titulo = models.CharField( 
        verbose_name='Titulo',                      
        max_length=300
    )

    url = models.CharField(
        verbose_name='url',
        null=True, 
        blank=True,
        max_length=1000  
    )

    embed_link = models.CharField(
        max_length=255,
        null=True, 
        blank=True
    )
    
    data_criacao = models.DateTimeField(
        verbose_name="Data Criação",
        auto_now_add=True
    )

    data_atualizacao = models.DateTimeField(
        verbose_name="Data Atualização",
        auto_now_add=True
    )

    descricao = models.TextField(
        verbose_name="Descrição",
        null=True, 
        blank=True
    )

    anexo = models.ImageField(
        verbose_name="Anexo",
        upload_to='anexo_conteudo/',
        null=True, 
        blank=True
    )

    autor = models.CharField(
        verbose_name='autor',
        max_length=200,
    )
    
    categoria = models.ForeignKey(
        Categoria, 
        verbose_name='categoria',
        on_delete=models.CASCADE,
    )

    usuario_criacao = models.ForeignKey(
		User, 
		related_name='%(class)s_requests_created',
		blank=True, null=True,
		default=None,
		on_delete=models.SET_NULL
	)

    usuario_atualizacao = models.ForeignKey(
		User, 
		related_name='%(class)s_requests_modified',
		blank=True, null=True,
		default=None,
		on_delete=models.SET_NULL
	)
    
    def save(self, *args, **kwargs):
        '''Sobrescrita do método save para realizarmos ações personalizadas.'''
        from crum import get_current_user
    
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.usuario_criacao = user
        self.usuario_atualizacao = user
    
        super(Conteudo, self).save(*args, **kwargs)
    
    def __str__(self):
        return "{}".format(self.titulo)
    
    class Meta:
        app_label = 'conteudo'
        verbose_name = 'Conteudo'
        verbose_name_plural = 'Conteudos'
        


    
