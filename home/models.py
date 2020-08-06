from django import forms
from django.db import models
from django.core.mail import EmailMessage
from django.shortcuts import render
from django.template.loader import get_template
from django.contrib import messages

from wagtail.core.models import Page, Orderable
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, FieldRowPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.contrib.settings.models import BaseSetting, register_setting

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

class HomePage(AbstractEmailForm):

    template = 'home/home_page.html'

    def save(self, *args, **kwargs):

        if not self.from_address:
            self.from_address = 'info@uniekgroen.be'

        super(HomePage, self).save(*args, **kwargs)

    def projects(self):

        realisaties = []

        for item in Realisatie.objects.all():
            if item.show:
                realisaties.append(item)

        return realisaties

    def serve(self, request, *args, **kwargs):

        ctx = self.get_context(request)
        ctx['projects'] = self.projects()

        if request.method == 'POST':
            form = self.get_form(request.POST, page=self, user=request.user)
            
            if form.is_valid():
                self.process_form_submission(form)
                ctx['form'] = self.get_form(page=self, user=request.user)
                messages.success(request, self.thank_you_text)
                return render(request, self.get_landing_page_template(request), ctx)

            else: 
                ctx['form'] = form
                return render(request, self.get_landing_page_template(request), ctx)

        form = self.get_form(page=self, user=request.user)

        ctx['form'] = form 

        return render(request, self.get_template(request), ctx)

    def send_mail(self, form):

        subject = self.subject
        receivers = [self.to_address, ]
        sender = self.from_address

        ctx = {}
        ctx['form'] = form
        content = get_template('home/mails/contact_form.html').render(ctx)
        
        msg = EmailMessage(subject, content, to=receivers, from_email=sender)
        msg.content_subtype = 'html'
        msg.send()

    def get_landing_page_template(self, request, *args, **kwargs):
        return self.template

    # Intro
    intro_image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        related_name='+',
        null=True,
        blank=True
    )

    # Section 1: Who are we? 
    section_1_title = models.CharField(verbose_name='Sectie 1', max_length=64, default='')
    section_1_image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        related_name='+',
        null=True,
        blank=True
    )

    section_1_description = models.TextField('Informatie', default="", blank=True)
    section_1_desc = RichTextField('Informatie', blank=True, null=True, features=['h5', 'h6', 'bold', 'italic', 'link', 'hr', 'blockquote'])


    # Section 2: What do we have to offer?
    section_2_title = models.CharField(verbose_name='Sectie 2', max_length=64, default='')

    section_2_subtitle1 = models.CharField(verbose_name='Ondertitel 1', max_length=64, default='All-in-one oplossing')
    section_2_desc_1 = RichTextField('Beschrijving 1', blank=True, null=True, features=['h5', 'h6', 'bold', 'italic', 'link', 'hr', 'blockquote'])
    section_2_image_part_1 = models.ForeignKey(
        'wagtailimages.Image',
        verbose_name='Achtergrond 1',
        on_delete=models.SET_NULL,
        related_name='+',
        null=True,
        blank=True
    )

    section_2_subtitle2 = models.CharField(verbose_name='Ondertitel 2', max_length=64, default='Ontwerpfase')
    section_2_desc_2 = RichTextField('Beschrijving 2', blank=True, null=True, features=['h5', 'h6', 'bold', 'italic', 'link', 'hr', 'blockquote'])
    section_2_image_part_2 = models.ForeignKey(
        'wagtailimages.Image',
        verbose_name='Achtergrond 2',
        on_delete=models.SET_NULL,
        related_name='+',
        null=True,
        blank=True
    )

    section_2_subtitle3 = models.CharField(verbose_name='Ondertitel 3', max_length=64, default='Realisatie')
    section_2_desc_3 = RichTextField('Beschrijving 3', blank=True, null=True, features=['h5', 'h6', 'bold', 'italic', 'link', 'hr', 'blockquote'])
    section_2_image_part_3 = models.ForeignKey(
        'wagtailimages.Image',
        verbose_name='Achtergrond 3',
        on_delete=models.SET_NULL,
        related_name='+',
        null=True,
        blank=True
    )

    section_2_subtitle4 = models.CharField(verbose_name='Ondertitel 4', max_length=64, default='Specialisaties')
    section_2_desc_4 = RichTextField('Beschrijving 4', blank=True, null=True, features=['h5', 'h6', 'bold', 'italic', 'link', 'hr', 'blockquote'])
    section_2_image_part_4 = models.ForeignKey(
        'wagtailimages.Image',
        verbose_name='Achtergrond 4',
        on_delete=models.SET_NULL,
        related_name='+',
        null=True,
        blank=True
    )

    section_2_extra = models.CharField(verbose_name='Tekst', max_length=128, null=True)
    section_2_extra_image = models.ForeignKey(
        'wagtailimages.Image',
        verbose_name='Achtergrond',
        on_delete=models.SET_NULL,
        related_name='+',
        null=True,
        blank=True
    )

    # Section 3: How do we work?
    section_3_title = models.CharField(verbose_name='Sectie 3', max_length=64, default='')

    section_3_extra = models.CharField(verbose_name='Tekst', max_length=128, null=True)
    section_3_extra_image = models.ForeignKey(
        'wagtailimages.Image',
        verbose_name='Achtergrond',
        on_delete=models.SET_NULL,
        related_name='+',
        null=True,
        blank=True
    )


    # Section 4: Portfolio

    section_4_title = models.CharField(verbose_name='Sectie 4', max_length=64, default='')

    section_4_extra = models.CharField(verbose_name='Tekst', max_length=128, null=True)
    section_4_extra_image = models.ForeignKey(
        'wagtailimages.Image',
        verbose_name='Achtergrond',
        on_delete=models.SET_NULL,
        related_name='+',
        null=True,
        blank=True
    )

    # Contact

    thank_you_text = models.CharField(verbose_name='Bevestiging tekst', default='Bedankt voor je bericht!', max_length=160)

    contact_title = models.CharField(verbose_name='titel', max_length=32, default='Contacteer ons')


HomePage.content_panels = [
    MultiFieldPanel([
        FieldPanel('title', classname='col8'),
        FieldRowPanel([
            ImageChooserPanel('intro_image')
        ])
    ],  heading='Intro',
        classname='collapsible'
    ),
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
        ImageChooserPanel('section_1_image'),
        FieldPanel('section_1_description', classname='col8'),
        FieldPanel('section_1_desc', classname='col8')
    ], 
        heading='Sectie 1',
        classname='collapsible collapsed'
    ),
    MultiFieldPanel([
        FieldPanel('section_2_subtitle1', classname='col8'),
        FieldPanel('section_2_desc_1', classname='col8'),
        FieldRowPanel([
            ImageChooserPanel('section_2_image_part_1'),
        ]),
        
        FieldPanel('section_2_subtitle2', classname='col8'),
        FieldPanel('section_2_desc_2', classname='col8'),
        FieldRowPanel([
            ImageChooserPanel('section_2_image_part_2'),
        ]),

        FieldPanel('section_2_subtitle3', classname='col8'),
        FieldPanel('section_2_desc_3', classname='col8'),
        FieldRowPanel([
            ImageChooserPanel('section_2_image_part_3'),
        ]),

        FieldPanel('section_2_subtitle4', classname='col8'),
        FieldPanel('section_2_desc_4', classname='col8'),
        FieldRowPanel([
            ImageChooserPanel('section_2_image_part_4'),
        ]),
    ], 
        heading='Sectie 2',
        classname='collapsible collapsed'
    ),
    MultiFieldPanel([
        FieldPanel('section_2_extra', classname='col8'),
        ImageChooserPanel('section_2_extra_image', classname='col8')
    ],
        heading='Sectie 2 - tussen tekst',
        classname='collapsible collapsed'
    ),
    MultiFieldPanel([
        InlinePanel('design_items')
    ], 
        heading='Sectie 3 - ontwerp traject',
        classname='collapsible collapsed'
    ),
    MultiFieldPanel([
        InlinePanel('implementation_items')
    ], 
        heading='Sectie 3 - realisatie traject',
        classname='collapsible collapsed'
    ),
    MultiFieldPanel([
        FieldPanel('section_3_extra', classname='col8'),
        ImageChooserPanel('section_3_extra_image', classname='col8')
    ],
        heading='Sectie 3 - tussen tekst',
        classname='collapsible collapsed'
    ),
    MultiFieldPanel([

    ],
        heading='Sectie 4 - realisaties',
        classname='collapsible collapsed'
    ),
    MultiFieldPanel([
        FieldPanel('section_4_extra', classname='col8'),
        ImageChooserPanel('section_4_extra_image', classname='col8')
    ],
        heading='Sectie 4 - tussen tekst',
        classname='collapsible collapsed'
    ),
    MultiFieldPanel(
        [
            FieldPanel('subject'),
            FieldPanel('thank_you_text'),
            FieldRowPanel([
                FieldPanel('to_address', classname='col6'),
                FieldPanel('from_address', classname='col6')
            ])
        ],
        heading='Contact: mail setup ',
        classname='collapsible collapsed'
    ),
    MultiFieldPanel(
        [
            InlinePanel('form_fields', label='Form fields'),
        ],
        heading='Contact: velden',
        classname='collapsible collapsed'
    )
]

HomePage.parent_page_types = []

HomePage.subpage_types = [
    'home.Realisatie'
]

class Realisatie(Page):

    locatie = models.ForeignKey(
        Locatie,
        on_delete=models.SET_NULL,
        null=True,
        related_name='+'
    )
    show = models.BooleanField(verbose_name='toon op homepage', default=False)

Realisatie.content_panels = [
    MultiFieldPanel([
        FieldPanel('title', classname='col8'),
        FieldPanel('locatie', classname='col8'),
        FieldPanel('show', classname='col8')
    ], heading='Algemene informatie'),
    MultiFieldPanel([
        InlinePanel('images')
    ], heading='Afbeeldingen')

]

class DesignItem(Orderable):
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='design_items')
    name = models.CharField(verbose_name='naam', max_length=255)
    description = models.TextField('beschrijving', default="", blank=True)
    desc = RichTextField('Beschrijving', blank=True, null=True, features=['h5', 'h6', 'bold', 'italic', 'link', 'hr', 'blockquote'])

DesignItem.panels = [
    FieldPanel('name'),
    FieldPanel('desc')
]

class ImplementationItem(Orderable):
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='implementation_items')
    name = models.CharField(verbose_name='naam', max_length=255)
    description = models.TextField('beschrijving', default="", blank=True)
    desc = RichTextField('Beschrijving', blank=True, null=True, features=['h5', 'h6', 'bold', 'italic', 'link', 'hr', 'blockquote'])

ImplementationItem.panels = [
    FieldPanel('name'),
    FieldPanel('desc')
]

class HomePageFormField(AbstractFormField):
    page = ParentalKey(HomePage, related_name='form_fields')

class RealisatieAfbeelding(Orderable):
    page = ParentalKey(Realisatie, on_delete=models.CASCADE, related_name='images')
    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        related_name='images',
        null=True
    )

RealisatieAfbeelding.panels = [
    ImageChooserPanel('image')
]