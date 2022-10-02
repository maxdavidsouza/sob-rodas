from django.db import models


class Agencia(models.Model):
    id = models.CharField(primary_key=True, max_length=18)
    nome = models.CharField(max_length=64)
    cependereco = models.ForeignKey('Endereco', models.DO_NOTHING, db_column='cepEndereco')
    gerente = models.ForeignKey('Funcionario', models.DO_NOTHING, db_column='gerente', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agencia'


class Cliente(models.Model):
    telefonefixo = models.CharField(db_column='telefoneFixo', max_length=30)
    telefonecelular = models.CharField(db_column='telefoneCelular', max_length=30, blank=True, null=True)
    cpfpessoa = models.OneToOneField('Pessoa', models.DO_NOTHING, db_column='cpfPessoa', primary_key=True)
    registrocnh = models.ForeignKey('Cnh', models.DO_NOTHING, db_column='registroCnh')

    class Meta:
        managed = False
        db_table = 'cliente'


class Cnh(models.Model):
    registro = models.CharField(primary_key=True, max_length=11)
    tipo = models.CharField(max_length=10)
    classificacao = models.CharField(max_length=2)
    validade = models.DateField(blank=True, null=True)
    datadeemissao = models.DateField(db_column='dataDeEmissao')

    class Meta:
        managed = False
        db_table = 'cnh'


class Contrato(models.Model):
    datadelocacao = models.DateTimeField(db_column='dataDeLocacao')
    dataderetorno = models.DateTimeField(db_column='dataDeRetorno')
    fechamento = models.CharField(max_length=8)
    cpfcliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='cpfCliente')
    cpffuncionario = models.ForeignKey('Funcionario', models.DO_NOTHING, db_column='cpfFuncionario')
    placaveiculo = models.ForeignKey('Veiculo', models.DO_NOTHING, db_column='placaVeiculo')

    class Meta:
        managed = False
        db_table = 'contrato'


class Endereco(models.Model):
    cep = models.CharField(primary_key=True, max_length=9)
    logradouro = models.CharField(max_length=64)
    bairro = models.CharField(max_length=64)
    cidade = models.CharField(max_length=64)
    estado = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'endereco'


class Funcionario(models.Model):
    horario = models.CharField(max_length=32)
    funcao = models.CharField(max_length=64)
    salario = models.FloatField()
    idagencia = models.ForeignKey(Agencia, models.DO_NOTHING, db_column='idAgencia')
    cpfpessoa = models.OneToOneField('Pessoa', models.DO_NOTHING, db_column='cpfPessoa', primary_key=True)

    class Meta:
        managed = False
        db_table = 'funcionario'


class Login(models.Model):
    usuario = models.CharField(max_length=64)
    senha = models.CharField(max_length=64)
    cpffuncionario = models.ForeignKey(Funcionario, models.DO_NOTHING, db_column='cpfFuncionario')

    class Meta:
        managed = False
        db_table = 'login'
        unique_together = (('id', 'cpffuncionario'),)


class Pagamento(models.Model):
    valor = models.FloatField()
    metodo = models.CharField(max_length=32)
    parcela = models.CharField(max_length=8)
    descricao = models.CharField(max_length=64)
    datadepagamento = models.DateTimeField(db_column='dataDePagamento')
    situacao = models.CharField(max_length=8)
    cpfpagador = models.ForeignKey('Pessoa', models.DO_NOTHING, db_column='cpfPagador')
    idcontrato = models.ForeignKey(Contrato, models.DO_NOTHING, db_column='idContrato')

    class Meta:
        managed = False
        db_table = 'pagamento'
        unique_together = (('id', 'cpfpagador', 'idcontrato'),)


class Pessoa(models.Model):
    cpf = models.CharField(primary_key=True, max_length=14)
    nome = models.CharField(max_length=64)
    datadenascimento = models.DateField(db_column='dataDeNascimento')
    numeroendereco = models.CharField(db_column='numeroEndereco', max_length=10, blank=True, null=True)
    cependereco = models.ForeignKey(Endereco, models.DO_NOTHING, db_column='cepEndereco')

    class Meta:
        managed = False
        db_table = 'pessoa'


class Seguro(models.Model):
    registro = models.CharField(primary_key=True, max_length=32)
    descricao = models.CharField(max_length=64)
    porcentagemarcada = models.FloatField(db_column='porcentagemArcada')
    valorpago = models.FloatField(db_column='valorPago')
    situacao = models.CharField(max_length=8)
    placaveiculo = models.ForeignKey('Veiculo', models.DO_NOTHING, db_column='placaVeiculo')

    class Meta:
        managed = False
        db_table = 'seguro'


class Veiculo(models.Model):
    placa = models.CharField(primary_key=True, max_length=8)
    tipo = models.CharField(max_length=32)
    modelo = models.CharField(max_length=64)
    marca = models.CharField(max_length=64)
    ano = models.PositiveIntegerField()
    quilometragem = models.FloatField()
    disponibilidade = models.IntegerField()
    valordiaria = models.FloatField(db_column='valorDiaria')
    valorquilometragem = models.FloatField(db_column='valorQuilometragem')
    idagencia = models.ForeignKey(Agencia, models.DO_NOTHING, db_column='idAgencia')

    class Meta:
        managed = False
        db_table = 'veiculo'


class Vistoria(models.Model):
    datadeefetuacao = models.DateField(db_column='dataDeEfetuacao')
    laudo = models.CharField(max_length=128)
    aprovacao = models.IntegerField()
    cpffuncionario = models.ForeignKey(Funcionario, models.DO_NOTHING, db_column='cpfFuncionario')
    placaveiculo = models.ForeignKey(Veiculo, models.DO_NOTHING, db_column='placaVeiculo')

    class Meta:
        managed = False
        db_table = 'vistoria'
        unique_together = (('id', 'cpffuncionario', 'placaveiculo'),)
