from django.db import models

from core.models.base import Base


class Skills(Base):
    __tablename__ = 'skills'

    skill_name = models.CharField('Nome da Habilidade', max_length=100, null=True, blank=True)
    icon = models.ImageField(upload_to='skills_icons/', null=True, blank=True)

    class Meta:
        verbose_name = 'Habilidade'
        verbose_name_plural = 'Habilidades'
        ordering = ['skill_name']
