# Generated by Django 4.2.1 on 2023-09-10 23:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, verbose_name='Titulo')),
                ('descricao', models.CharField(max_length=200, verbose_name='Descricao')),
                ('data_criacao', models.DateTimeField(auto_now_add=True, verbose_name='Data Criação')),
                ('data_atualizacao', models.DateTimeField(auto_now_add=True, verbose_name='Data Atualização')),
                ('usuario_atualizacao', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_requests_modified', to=settings.AUTH_USER_MODEL)),
                ('usuario_criacao', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_requests_created', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Conteudo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=300, verbose_name='Titulo')),
                ('descricao', models.CharField(max_length=1000, verbose_name='Descricao')),
                ('data_criacao', models.DateTimeField(auto_now_add=True, verbose_name='Data Criação')),
                ('data_atualizacao', models.DateTimeField(auto_now_add=True, verbose_name='Data Atualização')),
                ('texto', models.TextField(blank=True, null=True, verbose_name='Descrição')),
                ('anexo', models.ImageField(upload_to='anexo_conteudo/', verbose_name='Anexo')),
                ('autor', models.CharField(max_length=200, verbose_name='autor')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='conteudo.categoria', verbose_name='categoria')),
                ('usuario_atualizacao', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_requests_modified', to=settings.AUTH_USER_MODEL)),
                ('usuario_criacao', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_requests_created', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Conteudo',
                'verbose_name_plural': 'Conteudos',
            },
        ),
    ]