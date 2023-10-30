from django.db import models

from core.models.base import Base


class Contact(Base):
    __tablename__ = 'contact'

    location = models.CharField(max_length=255, verbose_name='Localização')
    email = models.EmailField(max_length=255, verbose_name='E-mail')
    phone = models.CharField(max_length=20, verbose_name='Telefone')

    class Meta:
        verbose_name = 'Informações de Contato'
        verbose_name_plural = 'Informações de Contato'

    def __str__(self):
        return self.location
