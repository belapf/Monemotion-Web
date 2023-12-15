# Generated by Django 4.2.1 on 2023-09-10 23:15

import accounts.models
from django.conf import settings
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('first_name', models.CharField(help_text='Nome é um campo obrigatorio', max_length=100, verbose_name='Nome')),
                ('last_name', models.CharField(help_text='Sobrenome é obrigatorio', max_length=100, verbose_name='Sobrenome')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='E-mail')),
                ('telefone', models.CharField(max_length=15, verbose_name='Telefone')),
                ('cep', models.CharField(blank=True, max_length=20, null=True, verbose_name='Cep')),
                ('cidade', models.CharField(blank=True, max_length=100, null=True, verbose_name='Cidade')),
                ('rua', models.CharField(blank=True, max_length=100, null=True, verbose_name='Rua')),
                ('bairro', models.CharField(blank=True, max_length=100, null=True, verbose_name='Bairro')),
                ('logadouro', models.CharField(blank=True, max_length=100, null=True, verbose_name='Logadouro')),
                ('numero', models.CharField(blank=True, max_length=30, null=True, verbose_name='Numero')),
                ('image', models.ImageField(blank=True, default='img/default_avatar.png', null=True, upload_to='profile_pictures', verbose_name='Imagem')),
                ('is_staff', models.BooleanField(default=True, verbose_name='Membro da equipe')),
                ('role', models.CharField(blank=True, choices=[('Admin', 'Admin'), ('Psicologo', 'Psicologo'), ('Professor', 'Professor'), ('Aluno', 'Aluno')], max_length=20, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'User',
            },
            managers=[
                ('objects', accounts.models.UsuarioManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Perfil',
                'verbose_name_plural': 'Perfil',
                'ordering': ['id'],
                'permissions': (('acessar_paginas_profile_psicologo', 'Acessar Paginas Profile Psicologo'), ('acessar_paginas_profile_estudante', 'Acessar Paginas Profile Estudante'), ('acessar_paginas_profile_professor', 'Acessar Paginas Profile Professor')),
            },
        ),
    ]
