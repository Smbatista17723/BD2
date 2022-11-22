import email
from django import forms
from django.forms.widgets import NumberInput

Tipos_Uti = [
    ('2', 'Cliente'),
    ('3', 'Comercial - Nivel 1'),
    ('4', 'Comercial - Nivel 2'),
    ('5', 'Parceiro'),
]

class FormUti(forms.Form):
    desig = forms.CharField(max_length=100)
    passwd = forms.CharField(max_length=100)

class Registo(forms.Form):
    nome = forms.CharField(max_length=30)
    apelido = forms.CharField(max_length=30)
    data_nascimento = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    morada = forms.CharField(max_length=50)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput(), max_length=16)
    tipo = forms.ChoiceField(choices=Tipos_Uti)

class Login(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput(), max_length=16)

class RegistoProd(forms.Form):
    nome_produto = forms.CharField(max_length=30)
    marca = forms.CharField(max_length=30)
    preço = forms.CharField(max_length=30)