# Generated by Django 2.2.6 on 2019-12-01 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_adres_locatie_websitesettings'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='websitesettings',
            options={'verbose_name': 'Algemene informatie'},
        ),
        migrations.AddField(
            model_name='homepage',
            name='section_1_title',
            field=models.CharField(default='', max_length=64, verbose_name='Titel sectie 1'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='section_2_title',
            field=models.CharField(default='', max_length=64, verbose_name='Titel sectie 2'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='section_3_title',
            field=models.CharField(default='', max_length=64, verbose_name='Titel sectie 3'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='section_4_title',
            field=models.CharField(default='', max_length=64, verbose_name='Titel sectie 4'),
        ),
    ]