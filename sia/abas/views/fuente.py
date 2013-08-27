# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from abas.models import Fuente
import json

# Todos los requerimientos
def lista_fuentes_json(request):
  fuentes = Fuente.objects.all()
  callback = request.GET.get('callback')
  response = []

  for fuente in fuentes:
    response.append({
      'id': fuente.id,
      'nombre': fuente.nombre
    })

  return HttpResponse(callback + '(' + json.dumps(response, cls = DjangoJSONEncoder) + ')', mimetype = 'application/json')