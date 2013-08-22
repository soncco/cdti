# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from abas.models import Requerimiento
import json

# Todos los requerimientos
def lista_requerimientos_json(request):
  requerimientos = Requerimiento.objects.all()
  callback = request.GET.get('callback')
  response = []

  for requerimiento in requerimientos:
    response.append({
      'id': requerimiento.id,
      'fecha': requerimiento.fecha,
      'numero': requerimiento.numero,
      'glosa': requerimiento.glosa,
      'creado_por': {
        'id': requerimiento.creado_por.id,
        'username': requerimiento.creado_por.username
      }
    })

  return HttpResponse(callback + '(' + json.dumps(response, cls = DjangoJSONEncoder) + ')', mimetype = 'application/json')