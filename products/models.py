# -*- coding: utf-8 -*-
from audioop import reverse
from django.db import models
from django.contrib.auth.models import User
class Product(models.Model):
    name = models.CharField('Name', max_length=200, unique=True  )
    description = models.TextField('Description', blank=True)
    link = models.CharField('Url Link', max_length=200, unique=True)
    price = models.DecimalField('Price', decimal_places=2, max_digits=8)
    author = models.CharField('Author', max_length=100)
    created = models.DateTimeField('Created', auto_now_add=True)
    changed = models.DateTimeField('Changed', auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse('product_edit', kwargs={'pk': self.pk})
