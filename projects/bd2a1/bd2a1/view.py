from django.shortcuts import render
from django.db import connection
from bd2a1.models import UtiModel
from .forms import FormUti, Login, Registo, RegistoProd
# Create your views here.

def showuti(request):
    showall=UtiModel.objects.all()
    return render(request, 'List.html', {"data": showall})
    
def home(request):
    return render(request, 'Index.html')

def set_uti(request):
        if request.method == 'POST':
            if request.POST.get('desig') and request.POST.get('passwd'):
                cursor = connection.cursor()
                cursor.execute("CALL insertUti('"+ request.POST.get('desig') +"', '"+ request.POST.get('passwd') +"')")
                connection.commit()
                cursor.close()
                form = FormUti()
                return render(request, 'Insert.html', {'form': form})
        else:
            form = FormUti()
            return render(request, 'Insert.html', {'form': form})   


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
            if request.POST.get('Data'):
                cursor = connection.cursor()
                cursor.execute("")
                connection.commit()
                cursor.close()
                form = RegistoProd()
                return render(request, 'Registo_Produtos.html', {'form': form})
        else:
            form = RegistoProd()
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