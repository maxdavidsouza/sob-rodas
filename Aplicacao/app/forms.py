from django.forms import ModelForm
from app.models import *

class EnderecoForm(ModelForm):
    class Meta:
        model = Endereco
        fields = ['cep', 'logradouro', 'bairro', 'cidade', 'estado']

class VeiculoForm(ModelForm):
    class Meta:
        model = Veiculo
        fields = ['placa', 'tipo', 'modelo', 'marca', 'ano', 'quilometragem', 'disponibilidade', 'valordiaria', 'valorquilometragem', 'idagencia']

class AgenciaForm(ModelForm):
    class Meta:
        model = Agencia
        fields = ['id', 'nome', 'cependereco', 'gerente']

class LoginForm(ModelForm):
    class Meta:
        model = Login
        fields = ['id', 'usuario', 'senha', 'cpffuncionario']

class PagamentoForm(ModelForm):
    class Meta:
        model = Pagamento
        fields = ['id', 'valor', 'metodo', 'parcela','descricao', 'datadepagamento', 'situacao', 'cpfpagador', 'idcontrato']

class VistoriaForm(ModelForm):
    class Meta:
        model = Vistoria
        fields = ['id', 'datadeefetuacao', 'laudo', 'aprovacao','cpffuncionario', 'placaveiculo']

class SeguroForm(ModelForm):
    class Meta:
        model = Seguro
        fields = ['registro', 'descricao', 'porcentagemarcada', 'valorpago', 'situacao', 'placaveiculo']

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['telefonefixo', 'telefonecelular', 'cpfpessoa', 'registrocnh']

class CnhForm(ModelForm):
    class Meta:
        model = Cnh
        fields = ['registro', 'tipo', 'classificacao', 'validade', 'datadeemissao']

class FuncionarioForm(ModelForm):
    class Meta:
        model = Funcionario
        fields = ['horario', 'funcao', 'salario', 'idagencia', 'cpfpessoa']

class ContratoForm(ModelForm):
    class Meta:
        model = Contrato
        fields = ['id', 'datadelocacao', 'dataderetorno', 'fechamento', 'cpfcliente', 'cpffuncionario', 'placaveiculo']

class PessoaForm(ModelForm):
    class Meta:
        model = Pessoa
        fields = ['cpf', 'nome', 'datadenascimento', 'numeroendereco', 'cependereco']