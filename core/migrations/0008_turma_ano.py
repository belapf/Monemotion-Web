# Generated by Django 4.2.1 on 2023-12-11 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_remove_modalidade_usuario_atualizacao_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='turma',
            name='ano',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.ano', verbose_name='Ano'),
        ),
    ]
