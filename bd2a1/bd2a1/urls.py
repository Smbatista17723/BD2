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
    path('Admin/Valid/<str:user>', view.admin_val, name="admin_val"),
    path('Admin/Del/<str:user>', view.admin_del, name="admin_del"),
    path('Comercial/', view.index_com, name="comercial"),
    path('Comercial/<str:prod>/', view.escolhe_forn, name="escolhe_forn"),
    path('Comercial/<str:prod>/<str:forn>/', view.pedir_stock, name="pedir_stock"),
    path('Waitlist/', view.waitlist, name="waitlist"),
    path('Waitlist/Valid/<int:e_id>/', view.valida, name="valida"),
    path('Waitlist/Cancel/<int:e_id>/', view.cancela, name="cancela"),
    path('MinhasEncomendas/', view.minhas_enc, name="minhasenc"),
    path('Vendas/', view.vendas, name="vendas"),
    path('Parceiro/', view.show_produtos3, name="parceiro"),
    path('Colaboradores/', view.colaboradores, name="colaboradores"),
    path('Colaboradores/Fornecedor/<str:forn>/', view.del_forn, name="del_forn"),
    path('Colaboradores/Colaborador/<str:forn>/', view.del_col, name="del_col"),
    path('RegistoFornecedores/', view.registforn, name="fornecedores")
]