# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.renderers import JSONRenderer
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from siteTour.models import lugarTuristico
from siteTour.serializers import lugarTuristicoSerializer


class JSONResponse(HttpResponse):
    """
    Una HttpResponse que convierte su contenido en JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

# listar y crear
@csrf_exempt
def lugar_list(request):
    if request.method == 'GET':
        lugar = lugarTuristico.objects.all()
        serializer = lugarTuristicoSerializer(lugar, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = lugarTuristicoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


# listar por departamento
@csrf_exempt
def lugar_xDepa(request, idepa):
    try:
        lugar = lugarTuristico.objects.filter(iddep_id = int(idepa))
    except lugarTuristico.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = lugarTuristicoSerializer(lugar, many=True)
        return JSONResponse(serializer.data)


# obtener, actualizar y eliminar
@csrf_exempt
def lugar_detail(request, pk):
    try:
        lugar = lugarTuristico.objects.get(pk=pk)
    except lugarTuristico.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = lugarTuristicoSerializer(lugar)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = lugarTuristicoSerializer(lugar, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        lugar.delete()
        return HttpResponse(status=204)