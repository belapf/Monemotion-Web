# Generated by Django 4.2.1 on 2023-09-24 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conteudo', '0003_remove_conteudo_texto_conteudo_url_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='tag',
            field=models.CharField(blank=True, choices=[('Noticia', 'Noticia'), ('Video', 'Video'), ('Podcast', 'Podcast'), ('outros', 'outros')], max_length=50, null=True),
        ),
    ]
