from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import UserManager, AbstractUser
from django.db import models
from core.models.ano import Ano
from core.models.turma import Turma  
from core.models.curso import Curso


class Etnia(models.Model):
    nome = models.CharField(
        verbose_name="Nome",
        max_length=100,
    )

    def __str__(self):
        """Método que retorna a representação do objeto como string."""
        return self.nome

    class Meta:
        """Sub classe para definir meta atributos da classe principal."""

        app_label = "accounts"
        verbose_name = "Etnia"
        verbose_name_plural = "Etnias"


class ClasseSocial(models.Model):
    nome = models.CharField(
        verbose_name="Nome",
        max_length=100,
    )

    descricao = models.CharField(
        verbose_name="Descrição",
        max_length=500,
    )

    def __str__(self):
        """Método que retorna a representação do objeto como string."""
        return self.nome

    class Meta:
        """Sub classe para definir meta atributos da classe principal."""

        app_label = "accounts"
        verbose_name = "ClasseSocial"
        verbose_name_plural = "Classe Social"


class UsuarioManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Email é obrigatório")
        email = self.normalize_email(email)
        username = email  # Atribui o valor do email ao campo "username"
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_staff", True)

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser precisa ter is_superuser=True")
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser precisa ter is_staff=True")
        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    ADMIN = "Admin"
    PSICOLOGO = "Psicologo"
    PROFESSOR = "Professor"
    ALUNO = "Aluno"

    ROLE_CHOICES = (
        (ADMIN, "Admin"),
        (PSICOLOGO, "Psicologo"),
        (PROFESSOR, "Professor"),
        (ALUNO, "Aluno"),
    )

    RURAL = "Zona Rural"
    URBANA = "Zona Hurbana"

    LOCALIDADE_CHOICES = (
        (RURAL, "Zona Rural"),
        (URBANA, "Zona Urbana"),
    )

    first_name = models.CharField(
        verbose_name=("Nome"),
        max_length=100,
        blank=False,
        help_text=("Nome é um campo obrigatorio"),
    )
    last_name = models.CharField(
        verbose_name=("Sobrenome"),
        max_length=100,
        blank=False,
        help_text=("Sobrenome é obrigatorio"),
    )
    email = models.EmailField("E-mail", unique=True)
    telefone = models.CharField("Telefone", max_length=15)
    cep = models.CharField("Cep", max_length=20, blank=True, null=True)
    cidade = models.CharField("Cidade", max_length=100, blank=True, null=True)
    rua = models.CharField("Rua", max_length=100, blank=True, null=True)
    bairro = models.CharField("Bairro", max_length=100, blank=True, null=True)
    logadouro = models.CharField("Logadouro", max_length=100, blank=True, null=True)
    numero = models.CharField("Numero", max_length=30, blank=True, null=True)
    image = models.ImageField(
        "Imagem",
        upload_to="profile_pictures",
        default="img/default_avatar.png",
        blank=True,
        null=True,
    )
    etnia = models.ForeignKey(
        Etnia, verbose_name=("Etnia"), on_delete=models.SET_NULL, null=True
    )
    classe_social = models.ForeignKey(
        ClasseSocial,
        verbose_name=("Classe Social"),
        on_delete=models.SET_NULL,
        null=True,
    )

    religiao = models.CharField("Religiao", max_length=100, blank=True, null=True)
    matricula = models.CharField("Matrícula", max_length=100, blank=True, null=True)
    is_staff = models.BooleanField("Membro da equipe", default=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, blank=True, null=True)
    localidade = models.CharField(
        max_length=40, choices=LOCALIDADE_CHOICES, blank=True, null=True
    )
    curso = models.ForeignKey(
        Curso, verbose_name="Curso", on_delete=models.SET_NULL, blank=True, null=True
    )
    ano = models.ForeignKey(
        Ano,
        verbose_name="Ano/Período",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def __str__(self):
        return self.email

    objects = UsuarioManager()

    def save(self, *args, **kwargs):
        if not self.username:  # Se o campo "username" estiver vazio
            self.username = self.email  # Atribuir o valor do email ao campo "username"
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "User"

    def __str__(self):
        return self.first_name or self.email

    def get_full_name(self):
        return str(self)

    def get_short_name(self):
        return str(self).split(" ")[0]


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        if self.user.first_name and self.user.last_name:
            return f"{self.user.first_name} {self.user.last_name}"
        else:
            return self.user.email

    @property
    def get_informacao_user(self):
        if self.user is not None:
            return self.user
        return None

    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfil"
        ordering = ["id"]
        permissions = (
            # Acessar paginas psicologos
            ("acessar_paginas_profile_psicologo", "Acessar Paginas Profile Psicologo"),
            ("acessar_paginas_profile_estudante", "Acessar Paginas Profile Estudante"),
            ("acessar_paginas_profile_professor", "Acessar Paginas Profile Professor"),
        )

class RelatorioPsicologico(models.Model):
    titulo = models.CharField(verbose_name="Título", max_length=255)
    imagem = models.ImageField(upload_to="relatorio_images", blank=True, null=True)
    turma = models.ForeignKey(
        Turma,
        verbose_name="Turma",
        on_delete=models.SET_NULL,
        blank=True, null=True
    )
    data_hora = models.DateTimeField(verbose_name="Data e Hora")
    relatorio = models.TextField(verbose_name="Relatório")

    psicologo = models.ForeignKey(
        User, 
        verbose_name="Psicólogo",
        limit_choices_to={'role': User.PSICOLOGO},
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Relatório Psicológico"
        verbose_name_plural = "Relatórios Psicológicos"


# Definição da classe AtivacaoUser com seus campos e métodos.
class AtivacaoUser(models.Model):
    # Campo para armazenar o token de ativação, com comprimento máximo de 255 caracteres e valor único gerado automaticamente.
    token = models.CharField(max_length=255, unique=True)

    # Chave estrangeira que relaciona um objeto AtivacaoUser a um objeto User, e nenhuma ação será tomada em cascata ao excluir o User.
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    # Campo de data e hora que registra a data de criação do objeto AtivacaoUser.
    created_at = models.DateTimeField(auto_now_add=True)

    # Campo de data e hora que registra a data de utilização do token de ativação, sendo atualizado automaticamente em cada salvamento.
    used_at = models.DateTimeField(auto_now=True)

    # Campo booleano que indica se o token de ativação está ativo ou não, o valor padrão é False.
    active = models.BooleanField(default=False)

    # Método que retorna o nome de usuário do usuário associado, usado para representar o objeto como uma string.
    def __str__(self):
        return self.user.username

    # Subclasse Meta para definir metadados da classe principal.
    class Meta:
        # Nome do aplicativo que contém esse modelo.
        app_label = "accounts"
        # Nome legível para o modelo no singular.
        verbose_name = "Ativação de Usuário"
        # Nome legível para o modelo no plural.
        verbose_name_plural = "Ativação de Usuários"

