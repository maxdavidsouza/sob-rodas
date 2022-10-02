from django.contrib import admin
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import path
from django.views.generic import RedirectView

from app.views import *

urlpatterns = [

    #Rotas para Páginas Básicas de Interface Gráfica
    path('', menu_principal),

    #Rotas de Página de Listagem e Comunicação (GET) para o SGBD
    path('enderecos/', menu_enderecos),
    path('agencias/', menu_agencias),
    path('agencias/<path:id>/estoque', menu_estoques),
    path('veiculos/', menu_veiculos),
    path('vistorias/', menu_vistorias),
    path('seguros/', menu_seguros),
    path('funcionarios/', menu_funcionarios),
    path('login/', menu_login),
    path('clientes/', menu_clientes),
    path('cnh/', menu_cnh),
    path('contratos/', menu_contratos),
    path('pagamentos/', menu_pagamentos),
    path('pessoas/', menu_pessoas),

    #Rotas para Páginas de Cadastro de Dados
    path('enderecos/cadastro/', menu_endereco_cadastro),
    path('veiculos/cadastro/', menu_veiculos_cadastro),
    path('agencias/cadastro/', menu_agencias_cadastro),
    path('funcionarios/cadastro/', menu_funcionarios_cadastro),
    path('clientes/cadastro/', menu_clientes_cadastro),
    path('cnh/cadastro/', menu_cnh_cadastro),
    path('login/cadastro/', menu_login_cadastro),
    path('pessoas/cadastro/', menu_pessoas_cadastro),
    path('pagamentos/cadastro/', menu_pagamentos_cadastro),
    path('seguros/cadastro/', menu_seguros_cadastro),
    path('vistorias/cadastro/', menu_vistorias_cadastro),
    path('contratos/cadastro/', menu_contratos_cadastro),

    #Rotas de Comunicação (POST) para o SGBD
    path('criar-endereco/', criar_endereco),
    path('criar-veiculo/', criar_veiculo),
    path('criar-agencia/', criar_agencia),
    path('criar-funcionario/', criar_funcionario),
    path('criar-cliente/', criar_cliente),
    path('criar-cnh/', criar_cnh),
    path('criar-login/', criar_login),
    path('criar-pessoa/', criar_pessoa),
    path('criar-pagamento/', criar_pagamento),
    path('criar-seguro/', criar_seguro),
    path('criar-vistoria/', criar_vistoria),
    path('criar-contrato/', criar_contrato),

    #Rotas para Páginas de Alteração de Dados
    path('enderecos/edicao/<slug:pk>/', menu_endereco_edicao),
    path('agencias/edicao/<path:pk>/', menu_agencia_edicao),
    path('clientes/edicao/<path:pk>/', menu_cliente_edicao),
    path('funcionarios/edicao/<path:pk>/', menu_funcionario_edicao),
    path('login/edicao/<int:pk>/', menu_login_edicao),
    path('veiculos/edicao/<slug:pk>/', menu_veiculo_edicao),
    path('pessoas/edicao/<path:pk>/', menu_pessoa_edicao),

    #Rotas de Comunicação (PUT) para o SGBD
    path('editar-endereco/<slug:pk>/', editar_endereco),
    path('editar-agencia/<path:pk>/', editar_agencia),
    path('editar-cliente/<path:pk>/', editar_cliente),
    path('editar-funcionario/<path:pk>/', editar_funcionario),
    path('editar-login/<int:pk>/', editar_login),
    path('editar-veiculo/<slug:pk>/', editar_veiculo),
    path('editar-pessoa/<path:pk>/', editar_pessoa),

    #Rotas de Comunicação (DELETE) para o SGBD
    path('deletar-endereco/<slug:pk>/', deletar_endereco),
    path('deletar-agencia/<path:pk>/', deletar_agencia),
    path('deletar-veiculo/<slug:pk>/', deletar_veiculo),
    path('deletar-cliente/<path:pk>/<slug:pk2>/', deletar_cliente),
    path('deletar-funcionario/<path:pk>/', deletar_funcionario)

]
