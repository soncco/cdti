# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from abas.models import Area
import json

# Todos los requerimientos
def lista_areas_json(request):
  areas = Area.objects.all()
  callback = request.GET.get('callback')
  response = []

  for area in areas:
    response.append({
      'id': area.id,
      'nombre': area.nombre
    })

  return HttpResponse(callback + '(' + json.dumps(response, cls = DjangoJSONEncoder) + ')', mimetype = 'application/json')