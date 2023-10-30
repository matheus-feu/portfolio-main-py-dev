from django.db import models


class Base(models.Model):
    __tablename__ = 'base'

    created_at = models.DateTimeField('Criação', auto_now_add=True)
    modified_at = models.DateTimeField('Atualização', auto_now=True)
    active = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True
