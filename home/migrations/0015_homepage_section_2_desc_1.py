# Generated by Django 2.2.6 on 2020-01-10 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_homepage_contact_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='section_2_desc_1',
            field=models.TextField(blank=True, null=True, verbose_name='Beschrijving 1'),
        ),
    ]