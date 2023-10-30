from django.db import models
from stdimage import StdImageField

from core.models.base import Base


class Testimonials(Base):
    __tablename__ = 'testimonials'

    name = models.CharField('Nome', max_length=100)
    testimonial_text = models.TextField('Depoimento', max_length=500)
    position = models.CharField('Cargo', max_length=100)
    avatar = StdImageField('Avatar', upload_to='testimonials', variations={'thumbnail': {'width': 90, 'height': 90}})

    class Meta:
        verbose_name = 'Depoimento'
        verbose_name_plural = 'Depoimentos'
        ordering = ['name']

    def __str__(self):
        return self.name
