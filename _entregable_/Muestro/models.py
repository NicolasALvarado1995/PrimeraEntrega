from django.db import models
from django.db.models import Model
    
class Profesor(models.Model):
    name=models.CharField(max_length=40)
    lastname=models.CharField(max_length=40)
    def __str__(self):
        return f"{self.name}"

class Curso(models.Model):
    name=models.CharField(max_length=40)
    comision=models.IntegerField()
    def __str__(self):
        return f"{self.name}"
    

class Alumno(models.Model):#Datos ingresados a mano en la base de datos
    name=models.CharField(max_length=40)
    secondname= models.CharField(max_length=255, default="Some String")
    lastname=models.CharField(max_length=40)
    curso = models.ForeignKey(Curso, on_delete = models.CASCADE, related_name = "cursos", blank=True, null=True)
    profesor = models.ForeignKey(Profesor, on_delete = models.CASCADE, related_name = "profesores", blank=True, null=True)
