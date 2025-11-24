import mysql.connector
from dataclasses import dataclass

@dataclass
class Chave:
    def __init__(self):
        self.cnx = mysql.connector.connect(user='crud-user', password='crud-user', database='crud')
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
        self._nome_bairro = dados[6]
