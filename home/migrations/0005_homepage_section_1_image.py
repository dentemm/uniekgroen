# Generated by Django 2.2.6 on 2019-12-17 20:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0001_squashed_0021'),
        ('home', '0004_auto_20191201_1111'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='section_1_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
    ]