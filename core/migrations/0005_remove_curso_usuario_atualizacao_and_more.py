# Generated by Django 4.2.1 on 2023-09-17 20:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_turma_modalidade_curso_ano'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curso',
            name='usuario_atualizacao',
        ),
        migrations.RemoveField(
            model_name='curso',
            name='usuario_criacao',
        ),
    ]
