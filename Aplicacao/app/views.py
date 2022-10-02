from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *
from app.models import *
import datetime

# Procedimento que Retorna a Data e Hora atuais
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

# Página Principal
def menu_principal(request):
    return render(request, 'index.html')

# Página de Veículos
def menu_veiculos(request):
    data = {}
    data['db'] = Veiculo.objects.all()
    return render(request, 'veiculos.html', data)

# Página de Funcionários
def menu_funcionarios(request):
    data = {}
    data['db'] = Funcionario.objects.all()
    return render(request, 'funcionarios.html', data)

# Página de Endereços
def menu_enderecos(request):
    data = {}
    data['db'] = Endereco.objects.all()
    return render(request, 'enderecos.html', data)

# Página de Agências
def menu_agencias(request):
    data = {}
    data['db'] = Agencia.objects.all()
    return render(request, 'agencias.html', data)

# Página de Estoque da Agência X
def menu_estoques(request, id):
    data = {}
    data['db'] = Veiculo.objects.filter(idagencia=id)
    return render(request, 'estoques.html', data)

# Página de Contratos
def menu_contratos(request):
    data = {}
    data['db'] = Contrato.objects.all()
    return render(request, 'contratos.html', data)

# Página de Clientes
def menu_clientes(request):
    data = {}
    data['db'] = Cliente.objects.all()
    return render(request, 'clientes.html', data)

def menu_vistorias(request):
    data = {}
    data['db'] = Vistoria.objects.all()
    return render(request, 'vistorias.html', data)

def menu_seguros(request):
    data = {}
    data['db'] = Seguro.objects.all()
    return render(request, 'seguros.html', data)

def menu_pagamentos(request):
    data = {}
    data['db'] = Pagamento.objects.all()
    return render(request, 'pagamentos.html', data)

def menu_cnh(request):
    data = {}
    data['db'] = Cnh.objects.all()
    return render(request, 'cnh.html', data)

def menu_pessoas(request):
    data = {}
    data['db'] = Pessoa.objects.all()
    return render(request, 'pessoas.html', data)

def menu_login(request):
    data = {}
    data['db'] = Login.objects.all()
    return render(request, 'login.html', data)

def menu_endereco_cadastro(request):
    data = {}
    data['form'] = EnderecoForm()
    return render(request, 'enderecos-form.html', data)

def criar_endereco(request):
    menu_endereco_cadastro = EnderecoForm(request.POST or None)
    if menu_endereco_cadastro.is_valid():
        menu_endereco_cadastro.save()
        return menu_enderecos(request)

def menu_veiculos_cadastro(request):
    data = {}
    data['form'] = VeiculoForm()
    return render(request, 'veiculos-form.html', data)

def criar_veiculo(request):
    menu_veiculos_cadastro = VeiculoForm(request.POST or None)
    if menu_veiculos_cadastro.is_valid():
        menu_veiculos_cadastro.save()
        return menu_veiculos(request)

def menu_agencias_cadastro(request):
    data = {}
    data['form'] = AgenciaForm()
    return render(request, 'agencias-form.html', data)

def criar_agencia(request):
    menu_agencias_cadastro = AgenciaForm(request.POST or None)
    if menu_agencias_cadastro.is_valid():
        menu_agencias_cadastro.save()
        return menu_agencias(request)

def menu_funcionarios_cadastro(request):
    data = {}
    data['form'] = FuncionarioForm()
    return render(request, 'funcionarios-form.html', data)

def criar_funcionario(request):
    menu_funcionarios_cadastro = FuncionarioForm(request.POST or None)
    if menu_funcionarios_cadastro.is_valid():
        menu_funcionarios_cadastro.save()
        return menu_funcionarios(request)

def menu_clientes_cadastro(request):
    data = {}
    data['form'] = ClienteForm()
    return render(request, 'clientes-form.html', data)

def criar_cliente(request):
    menu_clientes_cadastro = ClienteForm(request.POST or None)
    if menu_clientes_cadastro.is_valid():
        menu_clientes_cadastro.save()
        return menu_clientes(request)

def menu_cnh_cadastro(request):
    data = {}
    data['form'] = CnhForm()
    return render(request, 'cnh-form.html', data)

def criar_cnh(request):
    menu_cnh_cadastro = CnhForm(request.POST or None)
    if menu_cnh_cadastro.is_valid():
        menu_cnh_cadastro.save()
        return menu_cnh(request)

def menu_login_cadastro(request):
    data = {}
    data['form'] = LoginForm()
    return render(request, 'login-form.html', data)

def criar_login(request):
    menu_login_cadastro = LoginForm(request.POST or None)
    if menu_login_cadastro.is_valid():
        menu_login_cadastro.save()
        return menu_login(request)

def menu_pessoas_cadastro(request):
    data = {}
    data['form'] = PessoaForm()
    return render(request, 'pessoas-form.html', data)

def criar_pessoa(request):
    menu_pessoas_cadastro = PessoaForm(request.POST or None)
    if menu_pessoas_cadastro.is_valid():
        menu_pessoas_cadastro.save()
        return menu_pessoas(request)

def menu_pagamentos_cadastro(request):
    data = {}
    data['form'] = PagamentoForm()
    return render(request, 'pagamentos-form.html', data)

def criar_pagamento(request):
    menu_pagamentos_cadastro = PagamentoForm(request.POST or None)
    if menu_pagamentos_cadastro.is_valid():
        menu_pagamentos_cadastro.save()
        return menu_pagamentos(request)

def menu_seguros_cadastro(request):
    data = {}
    data['form'] = SeguroForm()
    return render(request, 'seguros-form.html', data)

def criar_seguro(request):
    menu_seguros_cadastro = SeguroForm(request.POST or None)
    if menu_seguros_cadastro.is_valid():
        menu_seguros_cadastro.save()
        return menu_seguros(request)

def menu_vistorias_cadastro(request):
    data = {}
    data['form'] = VistoriaForm()
    return render(request, 'vistorias-form.html', data)

def criar_vistoria(request):
    menu_vistorias_cadastro = VistoriaForm(request.POST or None)
    if menu_vistorias_cadastro.is_valid():
        menu_vistorias_cadastro.save()
        return menu_vistorias(request)

def menu_contratos_cadastro(request):
    data = {}
    data['form'] = ContratoForm()
    return render(request, 'contratos-form.html', data)

def criar_contrato(request):
    menu_contratos_cadastro = ContratoForm(request.POST or None)
    if menu_contratos_cadastro.is_valid():
        menu_contratos_cadastro.save()
        return menu_contratos(request)

def menu_endereco_edicao(request, pk):
    data = {}
    data['db'] = Endereco.objects.get(cep=pk)
    data['form'] = EnderecoForm(instance=data['db'])
    return render(request, 'enderecos-form.html', data)

def editar_endereco(request, pk):
    data = {}
    data['db'] = Endereco.objects.get(cep=pk)
    form = EnderecoForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return menu_enderecos(request)

def menu_agencia_edicao(request, pk):
    data = {}
    data['db'] = Agencia.objects.get(id=pk)
    data['form'] = AgenciaForm(instance=data['db'])
    return render(request, 'agencias-form.html', data)

def editar_agencia(request, pk):
    data = {}
    data['db'] = Agencia.objects.get(id=pk)
    form = AgenciaForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return menu_agencias(request)

def menu_cliente_edicao(request, pk):
    data = {}
    data['db'] = Cliente.objects.get(cpfpessoa=pk)
    data['form'] = ClienteForm(instance=data['db'])
    return render(request, 'clientes-form.html', data)

def editar_cliente(request, pk):
    data = {}
    data['db'] = Cliente.objects.get(cpfpessoa=pk)
    form = ClienteForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return menu_clientes(request)

def menu_funcionario_edicao(request, pk):
    data = {}
    data['db'] = Funcionario.objects.get(cpfpessoa=pk)
    data['form'] = FuncionarioForm(instance=data['db'])
    return render(request, 'funcionarios-form.html', data)

def editar_funcionario(request, pk):
    data = {}
    data['db'] = Funcionario.objects.get(cpfpessoa=pk)
    form = FuncionarioForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return menu_funcionarios(request)

def menu_login_edicao(request, pk):
    data = {}
    data['db'] = Login.objects.get(id=pk)
    data['form'] = LoginForm(instance=data['db'])
    return render(request, 'login-form.html', data)

def editar_login(request, pk):
    data = {}
    data['db'] = Login.objects.get(id=pk)
    form = LoginForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return menu_login(request)

def menu_veiculo_edicao(request, pk):
    data = {}
    data['db'] = Veiculo.objects.get(placa=pk)
    data['form'] = VeiculoForm(instance=data['db'])
    return render(request, 'veiculos-form.html', data)

def editar_veiculo(request, pk):
    data = {}
    data['db'] = Veiculo.objects.get(placa=pk)
    form = VeiculoForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return menu_veiculos(request)

def menu_pessoa_edicao(request, pk):
    data = {}
    data['db'] = Pessoa.objects.get(cpf=pk)
    data['form'] = PessoaForm(instance=data['db'])
    return render(request, 'pessoas-form.html', data)

def editar_pessoa(request, pk):
    data = {}
    data['db'] = Pessoa.objects.get(cpf=pk)
    form = PessoaForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return menu_pessoas(request)

def deletar_endereco(request, pk):
    db = Endereco.objects.get(cep=pk)
    db.delete()
    return menu_enderecos(request)

def deletar_agencia(request, pk):
    db = Agencia.objects.get(id=pk)
    db.delete()
    return menu_agencias(request)

def deletar_veiculo(request, pk):
    db = Veiculo.objects.get(placa=pk)
    db.delete()
    return menu_veiculos(request)

def deletar_cliente(request, pk, pk2):
    db = Pessoa.objects.get(cpf=pk)
    db1 = Cliente.objects.get(cpfpessoa=pk)
    db2 = Cnh.objects.get(registro=pk2)
    db1.delete()
    db.delete()
    db2.delete()
    return menu_clientes(request)

def deletar_funcionario(request, pk):
    db = Pessoa.objects.get(cpf=pk)
    db1 = Funcionario.objects.get(cpfpessoa=pk)
    db1.delete()
    db.delete()
    return menu_funcionarios(request)