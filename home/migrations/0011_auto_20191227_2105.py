# Generated by Django 2.2.6 on 2019-12-27 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20191227_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='section_1_title',
            field=models.CharField(default='', max_length=64, verbose_name='Sectie 1'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='section_2_title',
            field=models.CharField(default='', max_length=64, verbose_name='Sectie 2'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='section_3_title',
            field=models.CharField(default='', max_length=64, verbose_name='Sectie 3'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='section_4_title',
            field=models.CharField(default='', max_length=64, verbose_name='Sectie 4'),
        ),
    ]
