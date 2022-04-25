from http.cookiejar import FileCookieJar
from multiprocessing import context
from unicodedata import name
from urllib import response
from django import forms
from django.views.generic import TemplateView
from typing import Any, Dict
from django.shortcuts import render
from requests import request
from _entregable_.Muestro.forms import DatosForms 
from _entregable_.Muestro.models import Alumno


class vista(TemplateView):
    
    
    Mostrar = 'htmls/index.html/'
    def get(self, request, status=None):#Envia informacion 
        context = {
            'Datos': Alumno.objects.all()
        }
        return render(request, self.Mostrar, context)


 
class formularioView(TemplateView):
    
    
    template_name = 'forms/Formulario.html'

    def get(self,request):
        context={
            'form':DatosForms()
        }
        return render(request, self.template_name,context)
    
    def post(self, request):#recibe indormacion
        
        response = DatosForms(request.POST)
        
        if response.is_valid():
            obj_response = response.cleaned_data
            
            name = obj_response['name']
            secondname = obj_response['secondname']
            lastname = obj_response['lastname']
            profesor = obj_response['profesor']
            curso = obj_response['curso']
            
            alumno = Alumno(name=name, secondname=secondname, lastname=lastname, profesor = profesor, curso = curso)
            alumno.save()

            
            
        context={
            'form': DatosForms()
        } 
        
        return render(request, self.template_name,context)


class Buscarview(TemplateView):
    template_name = 'forms/Buscar.html'
    
    def post(self, request):#este metodo recibe varios datos de un campo para mostrarla si es que existe
        
        context={
            "elements": Alumno.objects.filter(
                name=request.POST.get('name')
            ),
        }
        
        return render(request, self.template_name, context)
    
         