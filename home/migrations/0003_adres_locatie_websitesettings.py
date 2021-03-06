# Generated by Django 2.2.6 on 2019-11-17 19:39

from django.db import migrations, models
import django.db.models.deletion
import wagtail.search.index


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('wagtailimages', '0001_squashed_0021'),
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adres',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('woonplaats', models.CharField(max_length=40)),
                ('postcode', models.CharField(max_length=8)),
                ('straat', models.CharField(max_length=40)),
                ('huisnummer', models.CharField(max_length=8)),
                ('land', models.CharField(default='Belgium', max_length=64)),
            ],
            options={
                'verbose_name': 'adres',
                'verbose_name_plural': 'adressen',
                'ordering': ['woonplaats', 'straat'],
            },
        ),
        migrations.CreateModel(
            name='Locatie',
            fields=[
                ('adres_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='home.Adres')),
                ('naam', models.CharField(default='Uniek Groen', max_length=64, verbose_name='locatie naam')),
                ('longitude', models.DecimalField(blank=True, decimal_places=7, max_digits=10, null=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=7, max_digits=10, null=True)),
            ],
            options={
                'verbose_name': 'locatie',
                'verbose_name_plural': 'locaties',
                'ordering': ['naam'],
            },
            bases=('home.adres', wagtail.search.index.Indexed),
        ),
        migrations.CreateModel(
            name='WebsiteSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tagline', models.CharField(default='Tuinarchitectuur & Realisaties', max_length=255)),
                ('telefoon', models.CharField(blank=True, max_length=28)),
                ('email', models.EmailField(default='info@uniekgroen.be', max_length=254)),
                ('btw_nummer', models.CharField(blank=True, max_length=16, verbose_name='BTW nummer')),
                ('error_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site')),
                ('locatie', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='home.Locatie')),
            ],
            options={
                'verbose_name': 'Website settings',
            },
        ),
    ]
