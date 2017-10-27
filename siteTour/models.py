# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.utils.encoding import smart_unicode
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class region(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(blank = True)
    def __str__(self):
        return self.nombre
    def __unicode__(self):
        return smart_unicode(self.nombre)
    class Meta:
        # db_table  =  'region'
        ordering = ('id',)
        verbose_name = 'Region'
        verbose_name_plural ='Regiones'


@python_2_unicode_compatible
class departamento(models.Model):
    id = models.AutoField(primary_key=True)
    idreg = models.ForeignKey(region, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(blank = True)
    def __str__(self):
        return self.nombre
    def __unicode__(self):
        return self.nombre
    class Meta:
        # db_table  = 'departamento'
        # get_latest_by = 'id'
        ordering = ['idreg','nombre']
        verbose_name = 'Departamento'
        verbose_name_plural ='Departamentos'


@python_2_unicode_compatible
class lugarTuristico(models.Model):
    id = models.AutoField(primary_key=True)
    iddep = models.ForeignKey(departamento, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(blank = True)
    descripcion = models.TextField(blank=True, null=True)
    latitud = models.CharField(max_length=100)
    longitud = models.CharField(max_length=100)
    zoom = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre
    def __unicode__(self):
        return self.nombre
    class Meta:
        # db_table  = 'siteTour'
        # get_latest_by = 'id'
        ordering = ['iddep','nombre']
        verbose_name = 'Lugar Turistico'
        verbose_name_plural ='Lugares Turisticos'


