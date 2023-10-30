from django.db import models

from core.models.base import Base


class Projects(Base):
    github_url_project = models.URLField('URL do Projeto no GitHub', max_length=200, blank=True, null=True)
    category = models.CharField('Categoria', max_length=50, choices=(
        ('app', 'App'),
        ('card', 'Card'),
        ('web', 'Web'),
    ))

    class Meta:
        verbose_name = 'Projeto Pessoal'
        verbose_name_plural = 'Projetos Pessoais'
        ordering = ['-created_at']

    def __str__(self):
        return self.github_url_project
