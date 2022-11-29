from django.shortcuts import render
import pymongo
from django.db import connection
from .forms import FormUti, Login, Registo, RegistoProd
# Create your views here.

conexaomongo = pymongo.MongoClient("mongodb://localhost:27017/")["proj"]

def insere_produto(nome, tipo, quant, preco, forn, desconto):
        bd = conexaomongo
        col = bd["produtos"]
        doc = {"nome": nome,"tipo": tipo, "quantidade": quant, "fornecedor": forn, "preço": preco, "desconto": desconto}
        x = col.insert_one(doc)

def show_produtos(request):
    bd = conexaomongo
    col = bd["produtos"]
    x = col.find({},{"_id":(0)})
    return render(request, 'List.html', {"data": x})
    
def show_destaques(request):
    bd = conexaomongo
    col = bd["produtos"]
    x = col.find({"desconto": {"$gte": 10}},{"_id":(0)})
    return render(request, 'Index.html', {"data": x})

def regist(request):
    # if this is a POST request we need to process the form data
        if request.method == 'POST':
            if request.POST.get('Data'):
                cursor = connection.cursor()
                cursor.execute("")
                connection.commit()
                cursor.close()
                form = Registo()
                return render(request, 'Registo.html', {'form': form})
        else:
            form = Registo()
            return render(request, 'Registo.html', {'form': form})   

def registprod(request):
    # if this is a POST request we need to process the form data
        if request.method == 'POST':
            form = RegistoProd(request.POST)
            if form.is_valid():
                nomep = form.cleaned_data["nome"]
                tipop = form.cleaned_data["tipo"]
                quanti = form.cleaned_data["quantidade"]
                price = form.cleaned_data["preço"]
                forn = form.cleaned_data["fornecedor"]
                desc = form.cleaned_data["desconto"]
                insere_produto(nomep, tipop, quanti, price, forn, desc)
                return render(request, 'Registo_Produtos.html', {'form': form})
        else:
            form = RegistoProd(request.POST)
            return render(request, 'Registo_Produtos.html', {'form': form})   

def login(request):
    # if this is a POST request we need to process the form data
        if request.method == 'POST':
            if request.POST.get('Data'):
                cursor = connection.cursor()
                cursor.execute("")
                connection.commit()
                cursor.close()
                form = Login()
                return render(request, 'Login.html', {'form': form})
        else:
            form = Login()
            return render(request, 'Login.html', {'form': form})

def cart(request):
    #POR FAZER
    return render(request, 'Carrinho.html')  