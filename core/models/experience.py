from django.db import models

from core.choices import STATES
from core.models.base import Base


class Experience(Base):
    __tablename__ = 'experiences'

    company = models.CharField('Empresa', max_length=100)
    position = models.CharField('Cargo', max_length=100)
    location_experience = models.CharField('Localização', max_length=100, choices=STATES)
    date_start = models.CharField('Data de Início', max_length=10, blank=True, null=True)
    date_end = models.CharField('Data de Término', max_length=10, blank=True, null=True)
    task_1 = models.TextField('Tarefas', max_length=100, blank=True, null=True)
    task_2 = models.TextField('Tarefas', max_length=100, blank=True, null=True)
    task_3 = models.TextField('Tarefas', max_length=100, blank=True, null=True)
    current = models.BooleanField('Atual?', default=False)

    class Meta:
        verbose_name = 'Experiência Profissional'
        verbose_name_plural = 'Experiências Profissionais'
        ordering = ['-date_start']

    def __str__(self):
        return f'{self.company} ({self.date_start} - {self.date_end})'
