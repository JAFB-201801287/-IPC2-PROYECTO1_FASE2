from django import forms
from .models import *

class cliente(forms.Form):
    nombre_usuario = forms.CharField(required = True, max_length=20, help_text='', label='', widget=forms.TextInput(attrs={'placeholder': 'NOMBRE DE USUARIO'}))
    contrasena = forms.CharField(required = True, max_length=20, help_text='', label='', widget=forms.TextInput(attrs={'placeholder': 'CONTRASEÑA'}))
    cui = forms.IntegerField(required = True, help_text='', label='', widget=forms.TextInput(attrs={'placeholder': 'CUI'}))
    nit = forms.IntegerField(required = True, help_text='', label='', widget=forms.TextInput(attrs={'placeholder': 'NIT'}))
    nombre = forms.CharField(required = True, max_length=100, help_text='', label='', widget=forms.TextInput(attrs={'placeholder': 'NOMBRE'}))
    apellido = forms.CharField(required = True, max_length=100, help_text='', label='', widget=forms.TextInput(attrs={'placeholder': 'APELLIDO'}))
    fecha_nacimiento = forms.CharField(required = True, help_text='', label='FECHA DE NACIMIENTO', widget=forms.SelectDateWidget(years=range(1950, 2021)))


    class Meta:
        fields = ("nombre_usuario","contrasena", "cui","nit", "nombre", "apellido", "fecha_nacimiento")

class empresa(forms.Form):
    nombre_usuario = forms.CharField(required = True, max_length=20, help_text='', label='', widget=forms.TextInput(attrs={'placeholder': 'NOMBRE DE USUARIO'}))
    contrasena = forms.CharField(required = True, max_length=20, help_text='', label='', widget=forms.TextInput(attrs={'placeholder': 'CONTRASEÑA'}))
    nombre = forms.CharField(required = True, max_length=100, help_text='', label='', widget=forms.TextInput(attrs={'placeholder': 'NOMBRE DE EMPRESA'}))
    nombre_comercial = forms.CharField(required = True, max_length=100, help_text='', label='', widget=forms.TextInput(attrs={'placeholder': 'NOMBRE COMERCIAL'}))
    nombre_representante = forms.CharField(required = True, max_length=150, help_text='', label='', widget=forms.TextInput(attrs={'placeholder': 'NOMBRE DEL REPRESENTANTE'}))


    class Meta:
        fields = ("nombre_usuario","contrasena", "nombre", "nombre_comercial", "nombre_representante")
