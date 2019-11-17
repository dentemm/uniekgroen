from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, FieldRowPanel

class Adres(models.Model):

    woonplaats = models.CharField(max_length=40)
    postcode = models.CharField(max_length=8)
    straat = models.CharField(max_length=40)
    huisnummer = models.CharField(max_length=8)
    land = models.CharField(max_length=64, default='Belgium')

    class Meta:
        verbose_name = 'adres'
        verbose_name_plural = 'adressen'
        ordering = ['woonplaats', 'straat']
        
    def __str__(self):
        return '%s - %s' % (self.woonplaats, self.straat)

Adres.panels = [
		MultiFieldPanel([
				FieldRowPanel([
						FieldPanel('straat', classname='col8'),
						FieldPanel('huisnummer', classname='col4')
				]),
        FieldRowPanel([
            FieldPanel('woonplaats', classname='col8'),
            FieldPanel('postcode', classname='col4')
        ]),
		],
		heading='Adresinformatie'
		)
]