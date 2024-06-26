# Generated by Django 5.0.4 on 2024-05-13 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_remove_system_all_system_variables'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='system',
            options={'verbose_name': 'Sistema', 'verbose_name_plural': 'Sistemas'},
        ),
        migrations.AlterModelOptions(
            name='variable',
            options={'verbose_name': 'Variável', 'verbose_name_plural': 'Variáveis'},
        ),
        migrations.AlterField(
            model_name='system',
            name='acronym',
            field=models.CharField(max_length=10, unique=True, verbose_name='Sigla'),
        ),
        migrations.AlterField(
            model_name='system',
            name='contact_email',
            field=models.EmailField(max_length=100, verbose_name='E-mail de Contato'),
        ),
        migrations.AlterField(
            model_name='system',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='variable',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='variable',
            name='value',
            field=models.CharField(max_length=256, verbose_name='Valor'),
        ),
    ]
