# Generated by Django 4.2.1 on 2023-12-06 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_ativacaouser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('matricula', models.CharField(max_length=10)),
                ('curso', models.CharField(max_length=50)),
            ],
        ),
    ]