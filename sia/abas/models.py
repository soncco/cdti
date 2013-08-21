from django.db import models
from django.contrib.auth.models import User
from decimal import *


class Producto(models.Model):
  unidad_medida = models.CharField(max_length = 10)
  descripcion = models.CharField(max_length = 255)

  def __unicode__(self):
    return self.descripcion
