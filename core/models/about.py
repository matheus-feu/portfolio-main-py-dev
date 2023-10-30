from django.db import models
from stdimage.models import StdImageField

from core.models.base import Base


class About(Base):
    __tablename__ = 'about'

    name = models.CharField('Nome', max_length=100)
    title = models.TextField('Título', max_length=500)
    photo = StdImageField('Foto', upload_to='about', variations={'thumb': {'width': 600, 'height': 600, 'crop': True}})
    profession = models.CharField('Profissão', max_length=100)
    description_profession = models.TextField('Descrição da Profissão', max_length=500, null=True, blank=True)
    birth_date = models.DateField('Data de Nascimento', auto_now=False, auto_now_add=False)
    website = models.URLField('Website', max_length=100)
    phone = models.CharField('Telefone', max_length=20)
    city = models.CharField('Cidade', max_length=100)
    age = models.IntegerField('Idade')
    degree = models.CharField('Grau', max_length=100)
    email = models.EmailField('E-mail', max_length=100)
    freelance = models.BooleanField('Freelance?', default=True)
    objective = models.TextField('Objetivo', max_length=500, null=True, blank=True)
    description = models.TextField('Descrição', max_length=500, null=True, blank=True)

    linkedin = models.URLField('Linkedin', max_length=100, null=True, blank=True)
    github = models.URLField('Github', max_length=100, null=True, blank=True)
    facebook = models.URLField('Facebook', max_length=100, null=True, blank=True)
    instagram = models.URLField('Instagram', max_length=100, null=True, blank=True)
    twitter = models.URLField('Twitter', max_length=100, null=True, blank=True)
    skype = models.URLField('Skype', max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = 'Sobre Mim'
        verbose_name_plural = 'Sobre Mim'
