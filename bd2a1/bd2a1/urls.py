"""bd2a1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib import admin
from django.urls import include
from . import view
#Add URL maps to redirect the base URL to our application
from django.views.generic import RedirectView

urlpatterns = [
    path('', view.show_destaques, name="home"),
    path('Adiciona/<str:produto_nome>/', view.add_carrinho, name="adiciona"),
    path('Carrinho/Remove/<str:produto_nome>/', view.rmv_carrinho, name="remove"),
    path('Carrinho/Delete/<str:produto_nome>/', view.del_carrinho, name="delete"),
    path('Registo/', view.registuti, name="regist"),
    path('Login/', view.login, name="login"),
    path('LoginAdmin/', view.loginad, name="loginad"),
    path('LoginComercial/', view.logincom, name="logincom"),
    path('LoginParceiro/', view.loginpar, name="loginpar"),
    path('Carrinho/', view.show_carrinho, name="carrinho"),
    path('Produtos/', view.show_produtos, name="produtos"),
    path('Produtos/Adiciona/<str:produto_nome>/', view.add_carrinho, name="adiciona"),
    path('ProdComercial/', view.show_produtos2, name="prodcomercial"),
    path('RegistoProduto/', view.registprod, name="regist_prod"),
    path('RegistoProdutoParceiro/', view.registprod2, name="regist_prod2"),
    path('Finaliza/', view.finaliza, name="encomenda"),
    path('Clear/', view.limpa, name="limpa"),
    path('Logout/', view.logout, name="logout"),
    path('Perfil/', view.get_perfil ,name="perfil"),
    path('Admin/', view.index_admin, name="admin"),
    path('Comercial/', view.index_com, name="comercial"),
    path('EncAdmin', view.todas_enc, name="todasenc"),
    path('MinhasEncomendas', view.minhas_enc, name="minhasenc"),
    path('Parceiro', view.show_produtos3, name="parceiro")
]