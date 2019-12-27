from django import forms
from django.db import models

from wagtail.core.models import Page, Orderable
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.core.fields import RichTextField
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, FieldRowPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel

from modelcluster.models import ClusterableModel
from modelcluster.fields import ParentalKey, ParentalManyToManyField

from .snippets import Locatie, GenericItem
# from .helpers import GenericItem

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

    section_1_title = models.CharField(verbose_name='Sectie 1', max_length=64, default='')
    section_1_image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        related_name='+',
        null=True,
        blank=True
    )

    # Section 2: What do we have to offer?

    section_2_title = models.CharField(verbose_name='Sectie 2', max_length=64, default='')

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

    # Section 3: How do we work?

    section_3_title = models.CharField(verbose_name='Sectie 3', max_length=64, default='')

    # design_items = ParentalManyToManyField('home.GenericItem', blank=True)

    # Section 4: Portfolio

    section_4_title = models.CharField(verbose_name='Sectie 4', max_length=64, default='')


HomePage.content_panels = Page.content_panels + [
    MultiFieldPanel([
        FieldRowPanel([
            FieldPanel('section_1_title', classname='col6'),
            FieldPanel('section_2_title', classname='col6'),
            FieldPanel('section_3_title', classname='col6'),
            FieldPanel('section_4_title', classname='col6')
        ]),
    ], 
        heading='Algemeen',
        classname='collapsible'
    ),
    MultiFieldPanel([
        ImageChooserPanel('section_1_image')
    ], 
        heading='Sectie 1',
        classname='collapsible collapsed'
    ),
    MultiFieldPanel([
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
        InlinePanel('design_items')
    ], 
        heading='Sectie 3 - ontwerp traject',
        classname='collapsible collapsed'
    ),
]

# class HomePageDesignItem(models.Model):
#     page = ParentalKey('home.HomePage', on_delete=models.CASCADE, related_name='design_items')
#     item = models.ForeignKey(
#         GenericItem, on_delete=models.CASCADE, related_name='blog_pages')

#     class Meta:
#         unique_together = ('page', 'item')

# HomePageDesignItem.panels = [
#         SnippetChooserPanel('item'),
#     ]

# class GenericItem(Orderable, models.Model):

#     item = models.CharField(max_length=64)
#     volgorde = models.IntegerField()

#     class Meta:
#         verbose_name = 'Item'
#         verbose_name_plural = 'Items'

# GenericItem.panels = [
#     MultiFieldPanel([
#         FieldRowPanel([
#             FieldPanel('item', classname='col6'),
#             FieldPanel('volgorde', classname='col6')
#         ])
#     ])
# ]

# class DesignItem(GenericItem):

#     page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='design_items')

# DesignItem.panels = [
#     MultiFieldPanel([
#         FieldRowPanel([
#             FieldPanel('item', classname='col6'),
#             FieldPanel('volgorde', classname='col6')
#         ])
#     ])
# ]

# class DesignItem(GenericItem):

#     design_item = ParentalKey(HomePage, verbose_name='ontwerp item', on_delete=models.CASCADE, related_name='items', null=True)

'''

issues with snippets and manytomany inline

https://docs.wagtail.io/en/v2.7/getting_started/tutorial.html#a-basic-blog 
https://stackoverflow.com/questions/53512343/is-wagtails-inlinepanel-compatible-w-a-non-page-model


https://www.accordbox.com/blog/wagtail-tip-1-how-replace-parentalmanytomanyfield-inlinepanel/



https://stackoverflow.com/questions/50209851/django-wagtail-admin-handle-many-to-many-with-through


Deze lijkt nog wel interessant, maar mss overkill ... 
https://stackoverflow.com/questions/57453957/render-wagtail-inlinepanel-on-non-page-model-without-using-snippet

'''


class DesignItem(Orderable):
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='design_items')
    name = models.CharField(verbose_name='naam', max_length=255)
    description = models.TextField('beschrijving', default="", blank=True)

DesignItem.panels = [
    FieldPanel('name'),
    FieldPanel('description')
]