# Generated by Django 4.2.1 on 2023-10-22 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conteudo', '0005_conteudo_embed_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conteudo',
            name='anexo',
            field=models.ImageField(blank=True, null=True, upload_to='anexo_conteudo/', verbose_name='Anexo'),
        ),
    ]
