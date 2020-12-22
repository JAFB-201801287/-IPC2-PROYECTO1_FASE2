from django import forms
from .models import *
from django.db.models import Q

class inicio_sesion(forms.Form):
    nombre_usuario = forms.CharField(required = True, max_length=20, help_text='', label='', widget=forms.TextInput(attrs={'placeholder': 'NOMBRE DE USUARIO', 'class': 'text_box'}))
    contrasena = forms.CharField(required = True, max_length=20, help_text='', label='', widget=forms.PasswordInput(attrs={'placeholder': 'CONTRASEÑA', 'class': 'text_box'}))

    class Meta:
        fields = ("nombre_usuario","contrasena")