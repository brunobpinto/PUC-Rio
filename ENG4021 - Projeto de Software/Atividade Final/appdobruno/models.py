from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class PontosTuristicos(models.Model):
  ponto_turistico = models.CharField(max_length=50)
  bairro = models.CharField(max_length=20)
  cidade = models.CharField(max_length=20)
  rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])


class CuidadosDicas(models.Model):
  cuidados = models.CharField(max_length=100)
  lugares_para_ter_cuidado = models.CharField(max_length=20)
  perigo = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])