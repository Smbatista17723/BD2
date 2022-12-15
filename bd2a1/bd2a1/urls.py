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
    path('Registo/', view.registuti, name="regist"),
    path('Login/', view.login, name="login"),
    path('Carrinho/', view.show_carrinho, name="carrinho"),
    path('Carrinho2/', view.show_carrinho2, name="carrinho2"),
    path('Produtos/', view.show_produtos, name="produtos"),
    path('Comercial/', view.show_produtos2, name="comercial"),
    path('RegistoProduto/', view.registprod, name="regist_prod")
]