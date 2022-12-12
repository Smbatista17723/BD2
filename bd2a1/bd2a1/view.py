from django.shortcuts import render
import pymongo
from django.db import connection
from django.shortcuts import redirect
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
    col2 = bd["carrinho"]
    z = col2.count_documents({})
    return render(request, 'List.html', {"data": x, 'conta': z})
    
def insere_uti(nome, apelido, data_nascimento, morada, email, password, tipo):
        bd = conexaomongo
        col = bd["utilizadores"]
        doc = {"nome": nome,"apelido": apelido, "data_nascimento": data_nascimento, "morada": morada, "email": email, "password": password, "tipo": tipo}
        x = col.insert_one(doc)    

def login_ut(email, password):
    bd = conexaomongo
    col = bd["utilizadores"]
    x = col.count_documents({"email": email, "password":password})
    return x

def get_username(email, password):
    bd = conexaomongo
    col = bd["utilizadores"]
    x = col.find({"email": email, "password":password},{"nome":(1), "apelido":(1), "_id":(0)})
    return x

def get_perfil(request, email, password):
    bd = conexaomongo
    col = bd["utilizadores"]
    x = col.find({"email": email, "password":password},{"password":(0), "tipo":(0), "_id":(0)})
    col2 = bd["carrinho"]
    z = col2.count_documents({})
    return render(request, 'Perfil.html', {'perf': x, 'conta': z})

def show_destaques(request):
    bd = conexaomongo
    col = bd["produtos"]
    x = col.find({"desconto": {"$lte": 0.99}},{"_id":(0)})
    y = col.find({},{"_id":(0)}).sort("quantidade", 1).limit(5)
    col2 = bd["carrinho"]
    z = col2.count_documents({})
    return render(request, 'Index.html', {'data': x, 'd': y, 'conta': z})

def show_destaques2(request, nome):
    bd = conexaomongo
    col = bd["produtos"]
    x = col.find({"desconto": {"$gte": 10}},{"_id":(0)})
    y = col.find({},{"_id":(0)}).sort("quantidade", 1).limit(5)
    col2 = bd["carrinho"]
    z = col2.count_documents({})
    return render(request, 'Index2.html', {'data': x, 'd': y, 'nom': nome, 'conta': z})

def show_carrinho(request):
    bd = conexaomongo
    col = bd["carrinho"]
    x = col.find({},{"_id":(0)})
    y = col.aggregate([{"$group": {"_id": 'null', "total": {"$sum": {"$round": [{"$multiply": [{"$toDouble": "$preço"}, "$quantidade", "$desconto"]}, 2]}}}}])
    z = col.count_documents({})
    return render(request, 'Carrinho.html', {'data': x, 'total': y, 'conta': z})

def registuti(request):
    # if this is a POST request we need to process the form data
        if request.method == 'POST':
            form = Registo(request.POST)
            if form.is_valid():
                nome = form.cleaned_data["nome"]
                apelido = form.cleaned_data["apelido"]
                data_nascimento = form.cleaned_data["data_nascimento"]
                morada = form.cleaned_data["morada"]
                email = form.cleaned_data["email"]
                password = form.cleaned_data["password"]
                tipo = form.cleaned_data["tipo"]
                insere_uti(nome, apelido, data_nascimento, morada, email, password, tipo)
                return render(request, 'Registo.html', {'form': form})
        else:
            form = Registo(request.POST)
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
            form = Login(request.POST)
            if form.is_valid():
                email = form.cleaned_data["email"]
                password = form.cleaned_data["password"]
                val = login_ut(email, password)
                if(val > 0):
                    #nome = get_username(email, password)
                    #return show_destaques2(request, nome)
                    return get_perfil(request, email, password)
                else:
                    pag = 'Login.html'
                    context = {'form': form}
                    return render(request, pag, context)
        else:
            form = Login(request.POST)
            pag = 'Login.html'
            context = {'form': form}
            return render(request, pag, context)

def cart(request):
    #POR FAZER
    return render(request, 'Carrinho.html')  