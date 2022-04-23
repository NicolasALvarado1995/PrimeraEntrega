from django.db import models
from django.db.models import Model

class Datos(models.Model):#Datos ingresados a mano en la base de datos
    name=models.CharField(max_length=40)
    secondname= models.CharField(max_length=255, default="Some String")
    lastname=models.CharField(max_length=40)
    comision=models.IntegerField()
    curso=models.CharField(max_length=40)
    profesor= models.CharField(max_length=255, default="Some String")