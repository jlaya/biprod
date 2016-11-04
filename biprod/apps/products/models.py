# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
import os

def content_file_products(instance, filename):
    return 'media/products/{0}/{1}'.format(instance, filename)

class Products(models.Model):
    """
        Clase para el registro de Productos
    """
    nombre = models.CharField(max_length=100, null=True, blank=True)
    descripcion = models.CharField(max_length=200, null=True, blank=True)
    stock = models.FloatField(null=True, blank=True)
    precio = models.FloatField(null=True, blank=True)
    foto = models.FileField(upload_to=content_file_products, null=True, blank=True)

    #Auditoria
    user_create = models.ForeignKey(User, null=True, blank=True, related_name='+')
    user_update = models.ForeignKey(User, null=True, blank=True, related_name='+')
    fecha_create = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    fecha_update = models.DateTimeField(auto_now_add=False, auto_now=True, null=True, blank=True)


def __unicode__(self):
        """ Retorna el string """
        return self.nombre
