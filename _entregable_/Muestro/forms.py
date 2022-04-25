from django import forms
#Este archivo crea formularios


class DatosForms(forms.Form):
    name = forms.CharField()
    