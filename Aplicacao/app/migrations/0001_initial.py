# Generated by Django 4.1 on 2022-09-19 17:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agencia',
            fields=[
                ('id', models.CharField(max_length=18, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=64)),
            ],
            options={
                'db_table': 'agencia',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cnh',
            fields=[
                ('registro', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=10)),
                ('classificacao', models.CharField(max_length=2)),
                ('validade', models.DateField(blank=True, null=True)),
                ('datadeemissao', models.DateField(db_column='dataDeEmissao')),
            ],
            options={
                'db_table': 'cnh',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Contrato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datadelocacao', models.DateTimeField(db_column='dataDeLocacao')),
                ('dataderetorno', models.DateTimeField(db_column='dataDeRetorno')),
                ('fechamento', models.CharField(max_length=8)),
            ],
            options={
                'db_table': 'contrato',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('cep', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('logradouro', models.CharField(max_length=64)),
                ('bairro', models.CharField(max_length=64)),
                ('cidade', models.CharField(max_length=64)),
                ('estado', models.CharField(max_length=64)),
            ],
            options={
                'db_table': 'endereco',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=64)),
                ('senha', models.CharField(max_length=64)),
            ],
            options={
                'db_table': 'login',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pagamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.FloatField()),
                ('metodo', models.CharField(max_length=32)),
                ('parcela', models.CharField(max_length=8)),
                ('descricao', models.CharField(max_length=64)),
                ('datadepagamento', models.DateTimeField(db_column='dataDePagamento')),
                ('situacao', models.CharField(max_length=8)),
            ],
            options={
                'db_table': 'pagamento',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('cpf', models.CharField(max_length=14, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=64)),
                ('datadenascimento', models.DateField(db_column='dataDeNascimento')),
                ('numeroendereco', models.CharField(blank=True, db_column='numeroEndereco', max_length=10, null=True)),
            ],
            options={
                'db_table': 'pessoa',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Seguro',
            fields=[
                ('registro', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('descricao', models.CharField(max_length=64)),
                ('porcentagemarcada', models.FloatField(db_column='porcentagemArcada')),
                ('valorpago', models.FloatField(db_column='valorPago')),
                ('situacao', models.CharField(max_length=8)),
            ],
            options={
                'db_table': 'seguro',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('placa', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=32)),
                ('modelo', models.CharField(max_length=64)),
                ('marca', models.CharField(max_length=64)),
                ('ano', models.PositiveIntegerField()),
                ('quilometragem', models.FloatField()),
                ('disponibilidade', models.IntegerField()),
                ('valordiaria', models.FloatField(db_column='valorDiaria')),
                ('valorquilometragem', models.FloatField(db_column='valorQuilometragem')),
            ],
            options={
                'db_table': 'veiculo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Vistoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datadeefetuacao', models.DateField(db_column='dataDeEfetuacao')),
                ('laudo', models.CharField(max_length=128)),
                ('aprovacao', models.IntegerField()),
            ],
            options={
                'db_table': 'vistoria',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('telefonefixo', models.CharField(db_column='telefoneFixo', max_length=30)),
                ('telefonecelular', models.CharField(blank=True, db_column='telefoneCelular', max_length=30, null=True)),
                ('cpfpessoa', models.OneToOneField(db_column='cpfPessoa', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='app.pessoa')),
            ],
            options={
                'db_table': 'cliente',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('horario', models.CharField(max_length=32)),
                ('funcao', models.CharField(max_length=64)),
                ('salario', models.FloatField()),
                ('cpfpessoa', models.OneToOneField(db_column='cpfPessoa', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='app.pessoa')),
            ],
            options={
                'db_table': 'funcionario',
                'managed': False,
            },
        ),
    ]
