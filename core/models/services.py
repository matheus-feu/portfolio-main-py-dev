from django.db import models

from core.choices import ICONS_CHOICES
from core.models.base import Base


class Services(Base):
    __tablename__ = 'services'

    icon = models.CharField('Ícone', max_length=50, choices=ICONS_CHOICES)
    service = models.CharField('Serviço', max_length=100)
    description = models.TextField('Descrição', max_length=500)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'
        ordering = ['service']

    def __str__(self):
        return self.service
