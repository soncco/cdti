from django.conf.urls import patterns, url


urlpatterns = patterns('abas.views',
  url(r'^requerimientos/json$', 'lista_requerimientos_json', name = 'lista_requerimientos_json'),
  url(r'^areas/json$', 'lista_areas_json', name = 'lista_areas_json'),
  url(r'^fuentes/json$', 'lista_fuentes_json', name = 'lista_fuentes_json'),
)