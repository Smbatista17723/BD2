import email
from django import forms
from django.forms.widgets import NumberInput

DATE_INPUT_FORMATS = ['%Y-%m-%d']

Tipos_Uti = [
    ('Cliente', 'Cliente'),
    ('Comercial - Nivel 1', 'Comercial - Nivel 1'),
    ('Comercial - Nivel 2', 'Comercial - Nivel 2'),
    ('Parceiro', 'Parceiro'),
]

Tipos_Produto = [
    ('Smartphones', 'Smartphones'),
    ('Cinema', 'Cinema'),
    ('Gaming', 'Gaming'),
    ('Computadores', 'Computadores'),
    ('Merch', 'Merch'),
    ('Educacional', 'Educacional'),
    ('Música', 'Música'),
    ('Literatura', 'Literatura'),
    ('Escritório', 'Escritório')
]

class FormUti(forms.Form):
    desig = forms.CharField(max_length=100)
    passwd = forms.CharField(max_length=100)

class Registo(forms.Form):
    nome = forms.CharField(max_length=30, required=False)
    apelido = forms.CharField(max_length=30, required=False)
    data_nascimento = forms.CharField(max_length=30, widget=NumberInput(attrs={'type': 'date'}), required=False)
    morada = forms.CharField(max_length=50, required=False)
    email = forms.EmailField(required=False)
    password = forms.CharField(widget=forms.PasswordInput(), max_length=16, required=False)
    tipo = forms.ChoiceField(choices=Tipos_Uti, required=False)

class Login(forms.Form):
    email = forms.EmailField(required=False)
    password = forms.CharField(widget=forms.PasswordInput(), max_length=16, required=False)

class RegistoProd(forms.Form):
    nome = forms.CharField(max_length=30, required=False)
    tipo = forms.ChoiceField(choices=Tipos_Produto, required=False)
    quantidade = forms.IntegerField(required=False)
    preço = forms.FloatField(required=False)
    fornecedor = forms.CharField(required=False)
    desconto = forms.FloatField(required=False)