# Generated by Django 4.1.5 on 2023-01-16 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(max_length=30)),
                ('cpf', models.IntegerField()),
                ('telefone', models.IntegerField()),
                ('sexo', models.CharField(choices=[('F', 'Feminino'), ('M', 'Masculino'), ('N', 'Nenhuma das opções')], max_length=1)),
                ('cep', models.IntegerField()),
                ('cidade', models.CharField(max_length=60)),
                ('estado', models.CharField(max_length=60)),
                ('logradouro', models.CharField(max_length=20)),
                ('criado', models.DateField(auto_now_add=True)),
            ],
        ),
    ]