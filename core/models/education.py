from django.db import models

from core.choices import STATES
from core.models.base import Base


class Education(Base):
    __tablename__ = 'education'

    school = models.CharField('Instituição de Ensino', max_length=100)
    year_start = models.CharField('Data de Início', max_length=100, blank=True, null=True)
    year_end = models.CharField('Data de Término', max_length=100, blank=True, null=True)
    degree = models.CharField('Grau', max_length=100)
    curse = models.CharField('Curso', max_length=100, blank=True)
    location_education = models.CharField('Localização', max_length=100, choices=STATES)
    description = models.TextField('Descrição', max_length=500)
    current = models.BooleanField('Atual?', default=False)

    class Meta:
        verbose_name = 'Educação'
        verbose_name_plural = 'Educação'
        ordering = ['-year_start']

    def __str__(self):
        return f'{self.school} {self.curse} ({self.year_start} - {self.year_end})'
