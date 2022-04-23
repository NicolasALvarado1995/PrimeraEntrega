from http.cookiejar import FileCookieJar
from django.views.generic import TemplateView
from typing import Any, Dict
from django.shortcuts import render

from _entregable_.Muestro.models import Datos


class vista(TemplateView):
    Mostrar = 'htmls/index.html/'
    def get(self, request, status=None):
        context = {
            'Datos': Datos.objects.all()
        }
        return render(request, self.Mostrar, context)