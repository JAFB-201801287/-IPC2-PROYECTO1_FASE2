from django import forms
from .models import *
from django.db.models import Q 

class inicio_sesion(forms.Form):
    nombre_usuario = forms.CharField(required = True, max_length=20, help_text='', label='', widget=forms.TextInput(attrs={'placeholder': 'NOMBRE DE USUARIO', 'class': 'text_box'}))
    contrasena = forms.CharField(required = True, max_length=20, help_text='', label='', widget=forms.PasswordInput(attrs={'placeholder': 'CONTRASEÑA', 'class': 'text_box'}))

    class Meta:
        fields = ("nombre_usuario","contrasena")

class transaccion(forms.Form):
    monto = forms.FloatField(required = True, help_text='', label='', widget=forms.NumberInput(attrs={'placeholder': 'MONTO'}))
    TIPOS_MONEDA = [('', 'SELECCIONAR TIPO DE MONEDA'), ('QUETZAL', 'QUETZAL'), ('DOLLAR', 'DOLLAR')]
    tipo_moneda = forms.ChoiceField(required = True, help_text='', label='', choices=TIPOS_MONEDA)
    cuenta = forms.ModelChoiceField(required = True, help_text='', label='', queryset=Cuenta.objects.all(), empty_label="SELECCIONE NUMERO DE CUENTA", to_field_name="id_cuenta")

    class Meta:
        fields = ("monto", "tipo_moneda", "cuenta")


class estado(forms.Form):
    cuenta = forms.ModelChoiceField(required = True, help_text='', label='', queryset=Cuenta.objects.all(), empty_label="SELECCIONE NUMERO DE CUENTA", to_field_name="id_cuenta")

    class Meta:
        fields = ("cuenta")