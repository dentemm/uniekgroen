# Generated by Django 2.2.6 on 2020-01-08 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_homepage_section_1_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='contact_title',
            field=models.CharField(default='Contacteer ons', max_length=32, verbose_name='titel'),
        ),
    ]
