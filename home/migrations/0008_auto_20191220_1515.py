# Generated by Django 2.2.6 on 2019-12-20 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0001_squashed_0021'),
        ('home', '0007_auto_20191220_1458'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='section_2_image_part_1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image', verbose_name='Achtergrond 1'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='section_2_image_part_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image', verbose_name='Achtergrond 2'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='section_2_image_part_3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image', verbose_name='Achtergrond 3'),
        ),
    ]
