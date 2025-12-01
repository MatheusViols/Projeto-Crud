from CRUD.Valida import Valida

import mysql.connector
from dataclasses import dataclass

@dataclass
class Chave:
    def __init__(self):
        self.cnx = mysql.connector.connect(user='crud-user',
                                           password='crud-user',
                                           database='crud',
                                           buffered=True)
        self.cursor = self.cnx.cursor()


@dataclass
class DadosJovem:
    def __init__(self, dados):
        self.CPF = dados[0]
        self.senha = dados[1]
        self.nome_comp = dados[2]
        self.data_nasc = dados[3]
        self.telefone = dados[4]
        self.endereco = dados[5]
        self.desc_user = dados[6]
        self.cod_area = dados[7]
        self.cod_bairro = dados[8]
        self.nome_area = dados[9]
        self.nome_bairro = dados[10]

@dataclass
class DadosEmpresa:
    def __init__(self, dados):
        self.CNPJ = dados[0]
        self.senha = dados[1]
        self.nome_emp = dados[2]
        self.endereco = dados[3]
        self.desc_emp = dados[4]
        self.cod_bairro = dados[5]
        self.nome_bairro = dados[6]

@dataclass
class DadosInstituicao:
    def __init__(self, dados):
        self.CNPJ = dados[0]
        self.senha = dados[1]
        self.nome_inst = dados[2]
        self.endereco = dados[3]
        self.desc_inst= dados[4]
        self.cod_bairro = dados[5]
        self.nome_bairro = dados[6]


@dataclass
class DadosVagas:
    def __init__(self, lista_vagas):
        self.dados = { 
                 f'{vaga[0]}':{
                             'nome':vaga[1],
                             'quant':vaga[2],
                             'desc':vaga[3],
                             'cod_area':vaga[4],
                             'cod_turno':vaga[5],
                             'cod_bairro':vaga[6],
                             'nome_area':vaga[7],
                             'nome_turno':vaga[8],
                             'nome_emp':vaga[9],
                             'nome_bairro':vaga[10]
                             } for vaga in lista_vagas
                }

@dataclass
class DadosCursos:
    def __init__(self, lista_cursos):
        self.dados = { 
                 f'{curso[0]}':{
                             'nome':curso[1],
                             'quant':curso[2],
                             'desc':curso[3],
                             'cod_area':curso[4],
                             'cod_turno':curso[5],
                             'cod_bairro':curso[6],
                             'nome_area':curso[7],
                             'nome_turno':curso[8],
                             'nome_emp':curso[9],
                             'nome_bairro':curso[10]
                             } for curso in lista_cursos
                }

@dataclass
class InputCPF():
    def __init__(self):
        while True:
            validar = Valida(Chave())
            input_CPF = input("CPF: ")

            if validar.CPF(input_CPF): 
                self.CPF = input_CPF
                break
            else: 
                continue


@dataclass
class InputValido():
    def __init__(self, msg_input, tipo_input):
        while True:
            validar = Valida(Chave())
            dado = input(f"{msg_input}\n-> ")

            match tipo_input:
                case 'CPF': 
                    validado = validar.CPF(dado)
                case 'CNPJ': 
                    validado = validar.CNPJ(dado)
                case 'nome': 
                    validado = validar.Nome(dado)
                case 'telefone': 
                    validado = validar.Telefone(dado)
                case 'bairro': 
                    validado = validar.Bairro(dado)
                case 'endereco': 
                    validado = validar.Endereco(dado)
                case 'area': 
                    validado = validar.Area(dado)
                case 'descricao': 
                    validado = validar.Desc(dado)
                case 'nome_curso': 
                    validado = validar.nomeCurso(dado)
                case 'nome_vaga': 
                    validado = validar.nomeVaga(dado)
                case 'turno': 
                    validado = validar.Turno(dado)
                case 'senha':
                    conf_dado = input("Confirme sua senha\n-> ")
                    validado = validar.Senha(dado, conf_dado)
                case 'sair':
                    break
                case _:
                    print("Tipo de input não encontrado")
                    return False

            if validado:
                self.dado = dado
                break
            else:
                continue

@dataclass
class InputDataValida:
    def __init__(self):
        while True:
            validar = Valida(Chave())

            input_dia = input("Dia: ")
            input_mes = input("Mês: ")
            input_ano = input("Ano: ")

            if validar.Data(input_dia, input_mes, input_ano):
                self.dado = f"{input_ano}-{input_mes}-{input_dia}"
                break
            else:
                continue


