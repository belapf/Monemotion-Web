# Generated by Django 4.2.1 on 2023-12-06 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emocao', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emocao',
            name='tipo_emocao',
            field=models.CharField(choices=[('Nojo 🤢', 'Nojo 🤢'), ('Feliz 😊', 'Feliz 😊'), ('Medo 😰', 'Medo 😰'), ('Triste 😢', 'Triste 😢'), ('Irritado 😡', 'Irritado 😡')], max_length=100, verbose_name='Nome'),
        ),
    ]
