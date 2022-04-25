from django import forms
from django.forms import ModelChoiceField

from _entregable_.Muestro.models import Curso, Profesor
#Este archivo crea formularios



class ProfesorChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s" % obj.name
    
class CursoChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s" % obj.name

class DatosForms(forms.Form):
    name = forms.CharField()
    lastname = forms.CharField()
    secondname = forms.CharField()
    profesor = ProfesorChoiceField(queryset=Profesor.objects.all(), empty_label=None)
    curso = CursoChoiceField(queryset=Curso.objects.all(), empty_label=None) 