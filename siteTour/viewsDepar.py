# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.renderers import JSONRenderer
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from siteTour.models import departamento
from siteTour.serializers import departamentoSerializer

class JSONResponse(HttpResponse):
    """
    Una HttpResponse que convierte su contenido en JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def departamento_list(request):
    if request.method == 'GET':
        dep = departamento.objects.all()
        serializer = departamentoSerializer(dep, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = departamentoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

# listar por region
@csrf_exempt
def depa_xRegion(request, idreg):
    try:
        dep = departamento.objects.filter(idreg_id = int(idreg))
    except departamento.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = departamentoSerializer(dep, many=True)
        return JSONResponse(serializer.data)



# obtener, actualizar y eliminar
@csrf_exempt
def departamento_detail(request, pk):
    try:
        dep = departamento.objects.get(pk=pk)
    except departamento.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = departamentoSerializer(dep)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = departamentoSerializer(dep, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        dep.delete()
        return HttpResponse(status=204)