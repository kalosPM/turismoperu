# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from siteTour.models import region, departamento, lugarTuristico

# Register your models here.

@admin.register(region)
class regionAdmin(admin.ModelAdmin):
	list_display = ('id', 'nombre', 'imagen')
	list_display_links =('id',)
	list_filter = ('nombre',)
	search_fields = ["nombre"]
	list_editable = ('nombre',)
	actions = ['delete_selected']
	class Meta:
		model=region


@admin.register(departamento)
class departamentoAdmin(admin.ModelAdmin):
	list_display = ('id','idreg', 'nombre','imagen',)
	list_display_links =('id',)
	list_filter = ('nombre',)
	search_fields = ["nombre"]
	list_editable = ('nombre',)
	class Meta:
		model=departamento

   
@admin.register(lugarTuristico)
class lugarTuristicoAdmin(admin.ModelAdmin):
	list_display = ('id','iddep', 'nombre', 'imagen', 'descripcion', 'latitud', 'latitud','longitud','zoom')
	list_display_links =('id',)
	list_filter = ('nombre',)
	search_fields = ["nombre"]
	list_editable = ('nombre',)
	actions = ['delete_selected']
	class Meta:
		model=lugarTuristico

