# Generated by Django 4.2.1 on 2023-09-16 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_localidade'),
    ]

    operations = [
        migrations.CreateModel(
            name='Etnia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
            ],
            options={
                'verbose_name': 'Etnia',
                'verbose_name_plural': 'Etnias',
            },
        ),
    ]
