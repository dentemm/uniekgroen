from django.db import models

from wagtail.core.models import Page
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, FieldRowPanel
from wagtail.images.edit_handlers import ImageChooserPanel

from modelcluster.models import ClusterableModel

from .snippets import Locatie

#
# WAGTAIL SETTINGS
#
@register_setting
class WebsiteSettings(ClusterableModel, BaseSetting):

    tagline = models.CharField(max_length=255, default='Tuinarchitectuur & Realisaties')
    telefoon = models.CharField(max_length=28, blank=True)
    email = models.EmailField(default='info@uniekgroen.be')
    btw_nummer = models.CharField(verbose_name='BTW nummer', max_length=16, blank=True)

    locatie = models.ForeignKey(
        Locatie,
        on_delete=models.SET_NULL,
        null=True,
        related_name='+'
        )

    error_image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        related_name='+',
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Algemene informatie'

WebsiteSettings.panels = [
    MultiFieldPanel(
        [
            FieldRowPanel([
                FieldPanel('email', classname='col6'),
                FieldPanel('telefoon', classname='col6')
            ]),
            FieldRowPanel([
                FieldPanel('locatie', classname='col6')
            ]),
            FieldRowPanel([
                FieldPanel('btw_nummer', classname='col6'),
            ]),
            FieldPanel('tagline')
        ], 
        heading='Algemene informatie'
    ),
    MultiFieldPanel([
        ImageChooserPanel('error_image')
    ],
        heading='Error pages (404 / 500)',
        classname='collapsible'
    )
]


class HomePage(Page):

    section_1_title = models.CharField(verbose_name='Titel sectie 1', max_length=64, default='')
    section_2_title = models.CharField(verbose_name='Titel sectie 2', max_length=64, default='')
    section_3_title = models.CharField(verbose_name='Titel sectie 3', max_length=64, default='')
    section_4_title = models.CharField(verbose_name='Titel sectie 4', max_length=64, default='')


HomePage.content_panels = Page.content_panels + [
    MultiFieldPanel([
        FieldRowPanel([
            FieldPanel('section_1_title', classname='col8')
        ])
    ], heading='Sectie 1'),
    MultiFieldPanel([
        FieldRowPanel([
            FieldPanel('section_2_title', classname='col8')
        ])
    ], heading='Sectie 2'),
    MultiFieldPanel([
        FieldRowPanel([
            FieldPanel('section_3_title', classname='col8')
        ])
    ], heading='Sectie 3'),
        MultiFieldPanel([
        FieldRowPanel([
            FieldPanel('section_4_title', classname='col8')
        ])
    ], heading='Sectie 4')
]