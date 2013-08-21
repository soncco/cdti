from django.db import models
from django.contrib.auth.models import User
from decimal import *

# Sistema
class Producto(models.Model):
  unidad_medida = models.CharField(max_length = 10)
  descripcion = models.CharField(max_length = 255)

  def __unicode__(self):
    return self.descripcion

class Fuente(models.Model):
  nombre = models.CharField(max_length = 100)

class Proyecto(models.Model):
  fuente = models.ManyToManyField(Fuente)
  anio = models.IntegerField()
  nombre = models.CharField(max_length = 255, default = '')

class Area(models.Model):
  nombre = models.CharField(max_length = 100)

class Usuario(models.Model):
  usuario = models.OneToOneField(User)
  area = models.ManyToManyField(Area)
  proyecto = models.ManyToManyField(Proyecto)

# Requerimientos
class Requerimiento(models.Model):
  numero = models.CharField(max_length = 10)
  fecha = models.DateField()
  glosa = models.TextField()
  creado_por = models.ForeignKey(Usuario)

class RequerimientoDetalle(models.Model):
  pertenece_a = models.ForeignKey(Requerimiento)
  producto = models.ForeignKey(Producto)
  cantidad = models.FloatField()

# Cotizaciones
class Proveedor(models.Model):
  razon_social = models.CharField(max_length = 255)
  direccion = models.CharField(max_length = 255)
  ruc = models.CharField(max_length = 11)
  email = models.CharField(max_length = 255)
  telefono = models.CharField(max_length = 20, default = '')

class SolicitudCotizacion(models.Model):
  TIPOS = (
    ('B', 'Bien'),
    ('S', 'Servicio'),
  )
  numero = models.CharField(max_length = 10)
  fecha = models.DateField()
  creado_por = models.ForeignKey(Usuario)
  tipo_contratacion = models.CharField(max_length = 1, choices = TIPOS, default = 'B')
  requerimiento = models.ForeignKey(Requerimiento, blank = True)
  glosa = models.TextField()

class DetalleSolicitudCotizacion(models.Model):
  pertenece_a = models.ForeignKey(SolicitudCotizacion)
  producto = models.ForeignKey(Producto)
  cantidad = models.FloatField()

class Cotizacion(models.Model):
  solicitud = models.ForeignKey(SolicitudCotizacion)
  proveedor = models.ForeignKey(Proveedor)
  fecha_creacion = models.DateField()
  plazo_entrega = models.CharField(max_length = 100)
  vigencia = models.CharField(max_length = 100)
  glosa = models.TextField()

class PrecioCotizacion(models.Model):
  pertenece_a = models.ForeignKey(Cotizacion)
  costo_de = models.OneToOneField(DetalleSolicitudCotizacion)
  marca = models.CharField(max_length = 200)
  precio_unitario = models.DecimalField(max_digits = 11, decimal_places = 2, default = Decimal('0.00'))

class BuenaPro(models.Model):
  cotizacion = models.ForeignKey(Cotizacion)
  fecha = models.DateField()
  justificacion = models.TextField()
  observaciones = models.TextField()