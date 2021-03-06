# Generated by Django 2.2.6 on 2019-12-20 13:52

from django.db import migrations, models
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_homepage_section_1_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='section_2_description1',
            field=wagtail.core.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='section_2_description2',
            field=wagtail.core.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='section_2_description3',
            field=wagtail.core.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='section_2_subtitle1',
            field=models.CharField(default='All-in-one oplossing', max_length=64, verbose_name='Subtitel 1'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='section_2_subtitle2',
            field=models.CharField(default='Ontwerpfase', max_length=64, verbose_name='Subtitel 2'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='section_2_subtitle3',
            field=models.CharField(default='Realisatie', max_length=64, verbose_name='Subtitel 3'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='section_1_title',
            field=models.CharField(default='', max_length=64, verbose_name='Titel'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='section_2_title',
            field=models.CharField(default='', max_length=64, verbose_name='Titel'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='section_3_title',
            field=models.CharField(default='', max_length=64, verbose_name='Titel'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='section_4_title',
            field=models.CharField(default='', max_length=64, verbose_name='Titel'),
        ),
    ]
