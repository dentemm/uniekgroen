# Generated by Django 2.2.6 on 2020-01-08 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_implementationitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='section_1_description',
            field=models.TextField(blank=True, default='', verbose_name='Informatie'),
        ),
    ]
