# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.renderers import JSONRenderer
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from siteTour.models import region
from siteTour.serializers import regionSerializer


class JSONResponse(HttpResponse):
    """
    Una HttpResponse que convierte su contenido en JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

# # listar y crear
@csrf_exempt
def region_list(request):
    if request.method == 'GET':
        reg = region.objects.all()
        serializer = regionSerializer(reg, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = regionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


# obtener, actualizar y eliminar
@csrf_exempt
def region_detail(request, pk):
    try:
        reg = region.objects.get(pk=pk)
    except region.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = regionTuristicoSerializer(reg)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = regionTuristicoSerializer(reg, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        reg.delete()
        return HttpResponse(status=204)

