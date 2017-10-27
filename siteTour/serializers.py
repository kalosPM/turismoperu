# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers
from . import models

# from .models import region
class regionSerializer(serializers.ModelSerializer):
    class Meta:
         model = models.region
         fields = ('id','nombre', 'imagen')

# from .models import departamento
class departamentoSerializer(serializers.ModelSerializer):
    class Meta:
         model = models.departamento
         fields = ('id','idreg', 'nombre','imagen')
       
# from .models import lugarTuristico
class lugarTuristicoSerializer(serializers.ModelSerializer):
    class Meta:
         model = models.lugarTuristico
         fields = ('id','iddep', 'nombre', 'imagen', 'descripcion', 'latitud', 'latitud','longitud','zoom')


