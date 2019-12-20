from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
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

    # Section 1: Who are we? 
    section_1_title = models.CharField(verbose_name='Titel', max_length=64, default='')
    section_1_image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        related_name='+',
        null=True,
        blank=True
    )

    # Section 2: What do we have to offer?

    section_2_title = models.CharField(verbose_name='Titel', max_length=64, default='')

    section_2_subtitle1 = models.CharField(verbose_name='Ondertitel 1', max_length=64, default='All-in-one oplossing')
    section_2_description_1 = models.TextField('Beschrijving 1', default="", blank=True)
    section_2_image_part_1 = models.ForeignKey(
        'wagtailimages.Image',
        verbose_name='Achtergrond 1',
        on_delete=models.SET_NULL,
        related_name='+',
        null=True,
        blank=True
    )

    section_2_subtitle2 = models.CharField(verbose_name='Ondertitel 2', max_length=64, default='Ontwerpfase')
    section_2_description_2 = models.TextField('Beschrijving 2', default="", blank=True)
    section_2_image_part_2 = models.ForeignKey(
        'wagtailimages.Image',
        verbose_name='Achtergrond 2',
        on_delete=models.SET_NULL,
        related_name='+',
        null=True,
        blank=True
    )

    section_2_subtitle3 = models.CharField(verbose_name='Ondertitel 3', max_length=64, default='Realisatie')
    section_2_description_3 = models.TextField('Beschrijving 1', default="", blank=True)
    section_2_image_part_3 = models.ForeignKey(
        'wagtailimages.Image',
        verbose_name='Achtergrond 3',
        on_delete=models.SET_NULL,
        related_name='+',
        null=True,
        blank=True
    )


    section_3_title = models.CharField(verbose_name='Titel', max_length=64, default='')
    section_4_title = models.CharField(verbose_name='Titel', max_length=64, default='')


HomePage.content_panels = Page.content_panels + [
    MultiFieldPanel([
        FieldRowPanel([
            FieldPanel('section_1_title', classname='col8')
        ]),
        ImageChooserPanel('section_1_image')
    ], 
        heading='Sectie 1',
        classname='collapsible collapsed'
    ),
    MultiFieldPanel([
        FieldRowPanel([
            FieldPanel('section_2_title', classname='col8')
        ]),
        FieldPanel('section_2_subtitle1', classname='col8'),
        FieldPanel('section_2_description_1', classname='col8'),
        FieldRowPanel([
            ImageChooserPanel('section_2_image_part_1'),
        ]),
        

        FieldPanel('section_2_subtitle2', classname='col8'),
        FieldPanel('section_2_description_2', classname='col8'),
        FieldRowPanel([
            ImageChooserPanel('section_2_image_part_2'),
        ]),

        FieldPanel('section_2_subtitle3', classname='col8'),
        FieldPanel('section_2_description_3', classname='col8'),
        FieldRowPanel([
            ImageChooserPanel('section_2_image_part_3'),
        ]),
    ], 
        heading='Sectie 2',
        classname='collapsible collapsed'
    ),
    MultiFieldPanel([
        FieldRowPanel([
            FieldPanel('section_3_title', classname='col8')
        ])
    ], 
        heading='Sectie 3',
        classname='collapsible collapsed'
    ),
        MultiFieldPanel([
        FieldRowPanel([
            FieldPanel('section_4_title', classname='col8')
        ])
    ], 
        heading='Sectie 4',
        classname='collapsible collapsed'
    ),
]