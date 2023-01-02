from django.shortcuts import render
import pymongo
from django.db import connection
from django.db import models
from bd2a1.models import Enc
from django.shortcuts import redirect
from .forms import FormUti, Login, Registo, RegistoProd, RegistoProdPar
# Create your views here.

conexaomongo = pymongo.MongoClient("mongodb://localhost:27017/")["proj"]

def session_name():
    bd = conexaomongo
    col2 = bd["session"]
    xx = col2.find({},{'_id': 0})
    for xxx in xx:
        col3 = bd["utilizadores"]
        yy = col3.find({'email': str(xxx["email"])},{'nome':(1), 'apelido':(1), '_id':(0)})
        for yyy in yy:
            nam = yyy["nome"]
            ape = yyy["apelido"]
            nome = nam + " " + ape
            return nome

def session_mail():
    bd = conexaomongo
    col = bd["session"]
    xx = col.find({},{'_id': 0})
    for xxx in xx:
        return str(xxx["email"])

def session():
    bd = conexaomongo
    col = bd["session"]
    x = col.count_documents({})
    return x

def checkemail(email):
    bd = conexaomongo
    col2 = bd["waitlist"]
    y = col2.count_documents({"email": email})
    return y

def checkemail2(email):
    bd = conexaomongo
    col = bd["utilizadores"]
    x = col.count_documents({"email": email})
    return x


def insere_produto(nome, tipo, quant, preco, forn, desconto):
        bd = conexaomongo
        col = bd["produtos"]
        doc = {"nome": nome,"tipo": tipo, "quantidade": quant, "fornecedor": forn, "preço": preco, "desconto": desconto}
        x = col.insert_one(doc)

def show_produtos(request):
    bd = conexaomongo
    col = bd["produtos"]
    x = col.find({"quantidade": {"$gt": 0}},{"_id":(0)})
    col2 = bd["carrinho"]
    zz = col2.aggregate([{"$group": {"_id": 'null', "total": {"$sum": "$quantidade"}}}])
    if col2.count_documents({}) == 0:
        z = int(0)
    else:
        for zzz in zz:
            z = int(zzz["total"])
    val = session()
    if val > 0:
        nome = session_name()
        return render(request, 'List2.html', {"data": x, 'conta': z, "nom": nome})
    return render(request, 'List.html', {"data": x, 'conta': z})

def show_produtos2(request):
    bd = conexaomongo
    col = bd["produtos"]
    x = col.find({},{"_id":(0)})
    val = session()
    if (val > 0):
        nome = session_name
    return render(request, 'ListCom.html', {"data": x, 'nom': nome})

def show_produtos3(request):
    val = session()
    if (val > 0):
        nome = session_name()
    bd = conexaomongo
    col = bd["produtos"]
    x = col.find({"fornecedor": nome},{"_id":(0)})
    return render(request, 'ListParceiro.html', {"data": x, 'nom': nome})
    
def insere_uti(nome, apelido, data_nascimento, morada, email, password, tipo):
        bd = conexaomongo
        col = bd["utilizadores"]
        doc = {"nome": nome,"apelido": apelido, "data_nascimento": data_nascimento, "morada": morada, "email": email, "password": password, "tipo": tipo}
        x = col.insert_one(doc)   

def espera_uti(nome, apelido, data_nascimento, morada, email, password, tipo):
        bd = conexaomongo
        col = bd["waitlist"]
        doc = {"nome": nome,"apelido": apelido, "data_nascimento": data_nascimento, "morada": morada, "email": email, "password": password, "tipo": tipo}
        x = col.insert_one(doc)    

def login_ut(email, password):
    bd = conexaomongo
    col = bd["utilizadores"]
    x = col.count_documents({"email": email, "password":password, "tipo": "Cliente"})
    return x

def login_ad(email, password):
    bd = conexaomongo
    col = bd["utilizadores"]
    x = col.count_documents({"email": email, "password":password, "tipo": "Admin"})
    return x

def login_com1(email, password):
    bd = conexaomongo
    col = bd["utilizadores"]
    x = col.count_documents({"email": email, "password":password, "tipo": "Comercial - Nível 1"})
    return x

def login_com2(email, password):
    bd = conexaomongo
    col = bd["utilizadores"]
    x = col.count_documents({"email": email, "password":password, "tipo": "Comercial - Nível 2"})
    return x

def login_par(email, password):
    bd = conexaomongo
    col = bd["utilizadores"]
    x = col.count_documents({"email": email, "password":password, "tipo": "Parceiro"})
    return x

def get_username(email, password):
    bd = conexaomongo
    col = bd["utilizadores"]
    x = col.find({"email": email, "password":password},{"nome":(1), "apelido":(1), "_id":(0)})
    return x

def get_perfil(request):
    bd = conexaomongo
    email = session_mail()
    col = bd["utilizadores"]
    x = col.find({"email": email},{"password":(0), "tipo":(0), "_id":(0)})
    col2 = bd["carrinho"]
    zz = col2.aggregate([{"$group": {"_id": 'null', "total": {"$sum": "$quantidade"}}}])
    if col2.count_documents({}) == 0:
        z = int(0)
    else:
        for zzz in zz:
            z = int(zzz["total"])
    return render(request, 'Perfil.html', {'perf': x, 'conta': z})

def del_carrinho(request, produto_nome):
    bd = conexaomongo
    col = bd["carrinho"]
    col.delete_one({"nome": produto_nome})
    zz = col.aggregate([{"$group": {"_id": 'null', "total": {"$sum": "$quantidade"}}}])
    if col.count_documents({}) == 0:
        z = int(0)
    else:
        for zzz in zz:
            z = int(zzz["total"])
    val = session()
    if val > 0:
        nome = session_name()
        return render(request, 'Eliminado2.html', {'conta': z, 'nom': nome})
    return render(request, 'Eliminado.html', {'conta': z})

def rmv_carrinho(request, produto_nome):
    bd = conexaomongo
    col = bd["carrinho"]
    x = col.find({"nome": produto_nome},{})
    for xx in x:
        if xx["quantidade"] > 1:
            quanti = xx["quantidade"]
            quanti = int(quanti - 1)
            col.update_one({"nome": produto_nome}, {"$set": {"quantidade": quanti}})
        else:
            col.delete_one({"nome": produto_nome})
    zz = col.aggregate([{"$group": {"_id": 'null', "total": {"$sum": "$quantidade"}}}])
    if col.count_documents({}) == 0:
        z = int(0)
    else:
        for zzz in zz:
            z = int(zzz["total"])
    val = session()
    if val > 0:
        nome = session_name()
        return render(request, 'Removido2.html', {'conta': z, 'nom': nome})
    return render(request, 'Removido.html', {'conta': z})

def add_carrinho(request, produto_nome):
    bd = conexaomongo
    col = bd["produtos"]
    x = col.find({"nome": produto_nome}, {})
    col2 = bd["carrinho"]
    for xx in x:
        compara = xx["quantidade"]
        if col2.count_documents({"nome": produto_nome}) == 0:
            doc = {"nome": xx["nome"], "quantidade": int(1), "preço": str(xx["preço"]), "desconto": xx["desconto"]}
            col2.insert_one(doc)
        else:
            pro = col2.find({"nome": produto_nome}, {"quantidade":(1)})
            for yy in pro:
                quanti = yy["quantidade"]
                quanti = int(quanti) + 1
            if quanti > compara:
                col2.update_one({"nome": produto_nome}, {"$set": {"quantidade": compara}})
            else:
                col2.update_one({"nome": produto_nome}, {"$set": {"quantidade": quanti}})
    col = bd["carrinho"]
    zz = col.aggregate([{"$group": {"_id": 'null', "total": {"$sum": "$quantidade"}}}])
    if col.count_documents({}) == 0:
        z = int(0)
    else:
        for zzz in zz:
            z = int(zzz["total"])
    val = session()
    if val > 0:
        nome = session_name()
        return render(request, 'Adicionado2.html', {'conta': z, 'nom': nome})
    return render(request, 'Adicionado.html', {'conta': z})


def show_destaques(request):
    bd = conexaomongo
    col = bd["produtos"]
    x = col.find({"quantidade": {"$gt": 0}, "desconto": {"$gt": 0.00}},{}).sort("desconto", 1).limit(5)
    y = col.find({"quantidade": {"$gt": 0}},{}).sort("quantidade", 1).limit(5)
    col2 = bd["carrinho"]
    zz = col2.aggregate([{"$group": {"_id": 'null', "total": {"$sum": "$quantidade"}}}])
    if col2.count_documents({}) == 0:
        z = int(0)
    else:
        for zzz in zz:
            z = int(zzz["total"])
    val = session()
    if (val > 0):
        nome = session_name
        return render(request, 'Index2.html', {'data': x, 'd': y, 'nom': nome, 'conta': z})
    return render(request, 'Index.html', {'data': x, 'd': y, 'conta': z})

def todas_enc(request):
    val = session()
    if (val > 0):
        nome = session_name
    cursor = connection.cursor()
    cursor.execute("Select * from enc_ad();")
    data = cursor.fetchall()
    cursor.close()
    return render(request, 'Encomendas.html', {'data': data,'nom': nome})

def minhas_enc(request):
    val = session()
    if (val > 0):
        nome = session_name
    email = session_mail()
    cursor = connection.cursor()
    cursor.execute("select * from minhas_enc('"+ email +"');")
    data = cursor.fetchall()
    cursor.close()
    return render(request, 'MinhasEnc.html', {'data': data,'nom': nome})

def limpa(request):
    bd = conexaomongo
    col = bd["carrinho"]
    col.delete_many({})
    val = session()
    if (val > 0):
        nome = session_name
        return render(request, 'Limpo2.html', {'nom': nome, 'conta': 0})
    return render(request, 'Limpo.html', {'conta': 0})

def finaliza(request):
    teste = session_mail()
    if teste is None:
        teste = 'guest'
    bd = conexaomongo
    col = bd["carrinho"]
    x = col.find({},{"_id":(0)})
    cursor = connection.cursor()
    y = col.aggregate([{"$group": {"_id": 'null', "total": {"$sum": {"$round": [{"$multiply": [{"$toDouble": "$preço"}, "$quantidade", {"$subtract": [1, "$desconto"]}]}, 2]}}}}])
    for tot in y:
        preco = tot["total"]
        cursor.execute("CALL insere_enc(%s,%s);", (str(teste), float(str(preco))))
    connection.commit()
    cursor.close()
    cursor2 = connection.cursor()
    cursor2.execute("select max(e_id) as id from encomendas where e_user like '"+ teste +"';")
    c = cursor2.fetchone()
    cursor2.close()
    cursor3 = connection.cursor()
    col2 = bd["produtos"]
    for result in x:
        nom = result["nome"]
        qua = int(result["quantidade"])
        preç = float(result["preço"])
        desc = float(str(result["desconto"]))
        cursor3.execute("CALL Insere_Prod(%s,%s,%s,%s,%s);", (nom, qua, preç, c, desc))
        xx = col2.find({"nome": nom}, {})
        for result2 in xx:
            col2.update_one({"nome": nom}, {"$set": {"quantidade": int(result2["quantidade"] - qua)}})
    connection.commit()
    cursor3.close()
    col.delete_many({"quantidade": {"$gt": 0}})
    val = session()
    if val > 0:
        nome = session_name()
        return render(request, 'Encomenda2.html', {'conta': 0, 'nom': nome})
    return render(request, 'Encomenda.html', {'conta': 0})

def show_carrinho(request):
    bd = conexaomongo
    col = bd["carrinho"]
    x = col.find({},{"_id":(0)})
    y = col.aggregate([{"$group": {"_id": 'null', "total": {"$sum": {"$round": [{"$multiply": [{"$toDouble": "$preço"}, "$quantidade", {"$subtract": [1, "$desconto"]}]}, 2]}}}}])
    zz = col.aggregate([{"$group": {"_id": 'null', "total": {"$sum": "$quantidade"}}}])
    if col.count_documents({}) == 0:
        z = int(0)
        val = session()
        if val > 0:
            nome = session_name()
            return render(request, 'CarrinhoVazio2.html', {'conta': z, 'nom': nome})
        return render(request, 'CarrinhoVazio.html', {'conta': z})
    else:
        for zzz in zz:
            z = int(zzz["total"])
    val = session()
    if val > 0:
        nome = session_name()
        return render(request, 'Carrinho2.html', {'data': x, 'total': y, 'conta': z, 'nom': nome})
    return render(request, 'Carrinho.html', {'data': x, 'total': y, 'conta': z})

def registuti(request):
        bd = conexaomongo
        col2 = bd["carrinho"]
        zz = col2.aggregate([{"$group": {"_id": 'null', "total": {"$sum": "$quantidade"}}}])
        if col2.count_documents({}) == 0:
            z = int(0)
        else:
            for zzz in zz:
                z = int(zzz["total"])
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
                # Mongo com o email e verificar se existe
                if checkemail(email) > 0 or checkemail2(email) > 0:
                    form = Registo(request.POST)
                    return render(request, 'Registo2.html', {'form': form, 'conta': z})
                else:  
                    if tipo == 'Cliente':
                        insere_uti(nome, apelido, data_nascimento, morada, email, password, tipo)
                        return render(request, 'Registo.html', {'form': form, 'conta': z})
                    else:
                        espera_uti(nome, apelido, data_nascimento, morada, email, password, tipo)
                        return render(request, 'Registo.html', {'form': form, 'conta': z})
        else:
            form = Registo(request.POST)
            return render(request, 'Registo.html', {'form': form, 'conta': z})   


def registprod(request):
    # if this is a POST request we need to process the form data
        val = session()
        if (val > 0):
            nome = session_name
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
                return render(request, 'Registo_Produtos.html', {'form': form, 'nom': nome})
        else:
            form = RegistoProd(request.POST)
            return render(request, 'Registo_Produtos.html', {'form': form, 'nom': nome})   

def registprod2(request):
    # if this is a POST request we need to process the form data
        val = session()
        if (val > 0):
            nome = session_name()
        if request.method == 'POST':
            form = RegistoProdPar(request.POST)
            if form.is_valid():
                nomep = form.cleaned_data["nome"]
                tipop = form.cleaned_data["tipo"]
                quanti = form.cleaned_data["quantidade"]
                price = form.cleaned_data["preço"]
                desc = form.cleaned_data["desconto"]
                insere_produto(nomep, tipop, quanti, price, nome, desc)
                return render(request, 'Registo_Produtos2.html', {'form': form, 'nom': nome})
        else:
            form = RegistoProdPar(request.POST)
            return render(request, 'Registo_Produtos2.html', {'form': form, 'nom': nome}) 

def logout(request):
    bd = conexaomongo
    col3 = bd["session"]
    email = session_mail()
    col3.delete_one({"email": email})
    col2 = bd["carrinho"]
    zz = col2.aggregate([{"$group": {"_id": 'null', "total": {"$sum": "$quantidade"}}}])
    if col2.count_documents({}) == 0:
        z = int(0)
    else:
        for zzz in zz:
            z = int(zzz["total"])
    return render(request, 'Logout.html', {'conta': z})

def login(request):
    # if this is a POST request we need to process the form data
        bd = conexaomongo
        col2 = bd["carrinho"]
        zz = col2.aggregate([{"$group": {"_id": 'null', "total": {"$sum": "$quantidade"}}}])
        if col2.count_documents({}) == 0:
            z = int(0)
        else:
            for zzz in zz:
                z = int(zzz["total"])
        if request.method == 'POST':
            form = Login(request.POST)
            if form.is_valid():
                email = form.cleaned_data["email"]
                password = form.cleaned_data["password"]
                val = login_ut(email, password)
                if(val > 0):
                    col3 = bd["session"]
                    col3.insert_one({"email": email})
                    return show_destaques(request)
                else:
                    pag = 'Login.html'
                    context = {'form': form, 'conta': z}
                    return render(request, pag, context)
        else:
            form = Login(request.POST)
            pag = 'Login.html'
            context = {'form': form, 'conta': z}
            return render(request, pag, context)

def index_admin(request):
    bd = conexaomongo
    col = bd["waitlist"]
    x = col.find({},{"_id":(0)})
    val = session()
    if (val > 0):
        nome = session_name
        return render(request, 'IndexAd.html', {'data': x, 'nom': nome})
    return render(request, 'IndexAd.html', {'data': x})

def loginad(request):
    # if this is a POST request we need to process the form data
        bd = conexaomongo
        col2 = bd["carrinho"]
        zz = col2.aggregate([{"$group": {"_id": 'null', "total": {"$sum": "$quantidade"}}}])
        if col2.count_documents({}) == 0:
            z = int(0)
        else:
            for zzz in zz:
                z = int(zzz["total"])
        if request.method == 'POST':
            form = Login(request.POST)
            if form.is_valid():
                email = form.cleaned_data["email"]
                password = form.cleaned_data["password"]
                val = login_ad(email, password)
                if(val > 0):
                    col3 = bd["session"]
                    col3.insert_one({"email": email})
                    return index_admin(request)
                else:
                    pag = 'LoginAd.html'
                    context = {'form': form, 'conta': z}
                    return render(request, pag, context)
        else:
            form = Login(request.POST)
            pag = 'LoginAd.html'
            context = {'form': form, 'conta': z}
            return render(request, pag, context)

def index_com(request):
    bd = conexaomongo
    col = bd["waitlist"]
    x = col.find({},{"_id":(0)})
    col = bd["produtos"]
    z = col.find({"desconto": {"$gt": 0.00}},{"_id":(0)}).sort("desconto", 1).limit(5)
    y = col.find({},{"_id":(0)}).sort("quantidade", 1).limit(5)
    val = session()
    if (val > 0):
        nome = session_name
        return render(request, 'IndexCom.html', {'data': x, 'nom': nome, 'data': z, 'd': y})
    return render(request, 'IndexAd.html', {'data': x, 'data': z, 'd': y})

def logincom(request):
    # if this is a POST request we need to process the form data
        bd = conexaomongo
        col2 = bd["carrinho"]
        zz = col2.aggregate([{"$group": {"_id": 'null', "total": {"$sum": "$quantidade"}}}])
        if col2.count_documents({}) == 0:
            z = int(0)
        else:
            for zzz in zz:
                z = int(zzz["total"])
        if request.method == 'POST':
            form = Login(request.POST)
            if form.is_valid():
                email = form.cleaned_data["email"]
                password = form.cleaned_data["password"]
                val = login_com1(email, password)
                val2 = login_com2(email, password)
                if val > 0 or val2 > 0:
                    col3 = bd["session"]
                    col3.insert_one({"email": email})
                    return index_com(request)
                else:
                    pag = 'LoginCom.html'
                    context = {'form': form, 'conta': z}
                    return render(request, pag, context)
        else:
            form = Login(request.POST)
            pag = 'LoginCom.html'
            context = {'form': form, 'conta': z}
            return render(request, pag, context)

def index_par(request):
    bd = conexaomongo
    val = session()
    if (val > 0):
        nome = session_name()
    col = bd["produtos"]
    x = col.find({"fornecedor": nome},{"_id":(0)})
    return render(request, 'ListParceiro.html', {'data': x, 'nom': nome})

def loginpar(request):
    # if this is a POST request we need to process the form data
        bd = conexaomongo
        col2 = bd["carrinho"]
        z = col2.count_documents({})
        if request.method == 'POST':
            form = Login(request.POST)
            if form.is_valid():
                email = form.cleaned_data["email"]
                password = form.cleaned_data["password"]
                val = login_par(email, password)
                if val > 0:
                    col3 = bd["session"]
                    col3.insert_one({"email": email})
                    return index_par(request)
                else:
                    pag = 'LoginPar.html'
                    context = {'form': form, 'conta': z}
                    return render(request, pag, context)
        else:
            form = Login(request.POST)
            pag = 'LoginPar.html'
            context = {'form': form, 'conta': z}
            return render(request, pag, context)

def cart(request):
    #POR FAZER
    return render(request, 'Carrinho.html')  