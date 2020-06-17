import geopy
import ssl

from django.db import models

from wagtail.core.models import Orderable
from wagtail.snippets.models import register_snippet
from wagtail.search import index
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, FieldRowPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel

from .helpers import Adres

@register_snippet
class Locatie(Adres, index.Indexed):

    naam = models.CharField(verbose_name='locatie naam', max_length=64, default='Uniek Groen')
    longitude = models.DecimalField(max_digits=10, decimal_places=7, blank=True, null=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=7, blank=True, null=True)
    
    class Meta:
		    verbose_name = 'locatie'
		    verbose_name_plural = 'locaties'
		    ordering = ['naam', ]
        
    def __str__(self):
		    return self.naam
        
    def save(self, *args, **kwargs):

        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        geopy.geocoders.options.default_ssl_context = ctx

        geolocator = geopy.geocoders.Nominatim()
            
        address_string = self.straat + ' ' + self.huisnummer + ' ' + self.postcode + ' ' + self.woonplaats + ' ' + str(self.land)

        loc = geolocator.geocode(address_string)
        
        if not isinstance(loc, geopy.location.Location):

            alternative = self.straat + ' ' + self.postcode + ' ' + self.woonplaats + ' ' + str(self.land)
            loc = geolocator.geocode(alternative)
            
        if isinstance(loc, geopy.location.Location):

            self.latitude = loc.latitude
            self.longitude = loc.longitude
            
        return super(Locatie, self).save(*args, **kwargs)

Locatie.panels = [
	  MultiFieldPanel([
			  FieldRowPanel([
					  FieldPanel('naam', classname='col6'),
				    ]	
			  ),
			  FieldRowPanel([
					  FieldPanel('straat', classname='col8'),
					  FieldPanel('huisnummer', classname='col4')
          ]),
        FieldRowPanel([
            FieldPanel('woonplaats', classname='col8'),
            FieldPanel('postcode', classname='col4')
        ]),
    ], heading='Locatie informatie')
]

@register_snippet
class GenericItem(Orderable, models.Model):

    item = models.CharField(max_length=64)

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'

GenericItem.panels = [
    MultiFieldPanel([
        FieldRowPanel([
            FieldPanel('item', classname='col6'),
        ])
    ])
]