from django.db import models
from accounts.models import User

class Emocao(models.Model):

    ROLE_CHOICES = (
        ('Nojo 🤢', 'Nojo 🤢'),
        ('Feliz 😊', 'Feliz 😊'),
        ('Medo 😰', 'Medo 😰'),
        ('Triste 😢', 'Triste 😢'),
        ('Irritado 😡', 'Irritado 😡'),
        
        
        
        
    )


    motivo = models.CharField(
        max_length = 25,
        verbose_name = 'Motivo',
    )

    descricao = models.TextField(
        max_length = 1000, 
        verbose_name = 'Descrição',
        default="Sem Descrição"
    )

    tipo_emocao = models.CharField(
        max_length = 100,             
        verbose_name = 'Nome',
        choices=ROLE_CHOICES,
    )

    data_criacao = models.DateTimeField(
        verbose_name="Data Criação",
        auto_now_add=True
    )
    
    data_atualizacao = models.DateTimeField(
        verbose_name="Data Atualização",
        auto_now_add=True
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
    
        super(Emocao, self).save(*args, **kwargs)

    def __str__(self):
        return "{}".format(self.motivo)

    class Meta:
        app_label = 'emocao'
        verbose_name = 'Emoção'
        verbose_name_plural = 'Emoções'