from django.db import models

# Create your models here.
class Saludo(models.Model):
    mensaje = models.CharField(max_length=128)
