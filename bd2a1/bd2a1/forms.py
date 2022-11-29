import email
from django import forms
from django.forms.widgets import NumberInput

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
    nome = forms.CharField(max_length=30, required=False)
    tipo = forms.ChoiceField(choices=Tipos_Produto, required=False)
    quantidade = forms.IntegerField(required=False)
    preço = forms.CharField(max_length=30, required=False)
    fornecedor = forms.CharField(required=False)
    desconto = forms.IntegerField(required=False)