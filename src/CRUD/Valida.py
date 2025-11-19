import re

import datetime
from datetime import date

import mysql.connector

class Valida:
    def __init__(self, cnx, cursor):
        self.__cnx = cnx
        self.__cursor = cursor

    def CPF(self, CPF):
        if not CPF:
            return False
        elif re.search(r'[^0-9]', CPF):
            print("Erro: CPF aceita apenas números")
            return False
        elif len(CPF) < 11:
            print("Erro: CPF tem o número fixo de 11 digitos")
            return False


        return True

    def CPFExiste(self, CPF):
        self.__cursor.execute(f"SELECT CPF FROM usuario WHERE CPF = '{CPF}';")
        fetch_CPF = self.__cursor.fetchone()
        if fetch_CPF and fetch_CPF[0] == CPF:
            return True

        return False



    def CNPJ(self, CNPJ):
        if not CNPJ:
            return False
        elif re.search(r'[^0-9]', CNPJ):
            print("Erro: CNPJ aceita apenas números")
            return False
        elif len(CNPJ) != 14:
            print("Erro: CNPJ tem o número fixo de 14 digitos")
            return False


        return True

    def CNPJEmpExiste(self, CNPJ):
        self.__cursor.execute(f"SELECT CNPJ FROM empresa WHERE CNPJ = '{CNPJ}';")
        fetch_CNPJ = self.__cursor.fetchone()
        if fetch_CNPJ and fetch_CNPJ[0] == CNPJ:
            return True
        return False


    def CNPJInstExiste(self, CNPJ):

        self.__cursor.execute(f"SELECT CNPJ FROM instituicao WHERE CNPJ = '{CNPJ}';")
        fetch_CNPJ = self.__cursor.fetchone()
        if fetch_CNPJ and fetch_CNPJ[0] == CNPJ:
            return True
        return False

    def Nome(self, nome_comp):
        if not nome_comp or nome_comp.isspace():
            return False

        return True

    def Data(self, dia, mes, ano):
        if not dia or not mes or not ano:
            return False
        elif " " in dia or " " in mes or " " in ano:
            print("Erro: Data não aceita uso de espaços")
            return False
        elif len(dia) != 2 or len(mes) != 2 or len(ano) != 4:
            print("Erro: Dia e mes devem conter dois digitos, ano deve conter 4")
            return False
        elif re.search(r'[^0-9]', dia) or re.search(r'[^0-9]', mes) or re.search(r'[^0-9]', ano):
            print("Erro: Data de nascimento aceita apenas números")
            return False

        try:
            datetime.datetime(year=int(ano), month=int(mes), day=int(dia))
        except ValueError:
            print("Erro: Data inválida")
            return False

        ano_atual = int(date.today().year)
        ano = int(ano)
        if (ano_atual - ano) < 18 or (ano_atual - ano) > 29:
            print("Erro: O programa é destinado apenas aos jovens entre 18 a 29 anos")
            return False


        return True

    def Telefone(self, telefone):
        if not telefone:
            print("Erro: telefone não pode ser vazio")
            return False
        elif " " in telefone:
            print("Erro: telefone não aceita espaços em branco")
            return False
        elif len(telefone) != 11:
            print("Erro: telefone tem um tamanho fixo de 11 digitos")
            return False
        elif re.search(r'[^0-9]', telefone):
            print("Erro: telefone aceita apenas números")
            return False

        return True



    def Bairro(self, bairro):
        if not bairro or bairro.isspace():
            print("Erro: Bairro não pode ser vazio")
            return False
        elif re.search(r'[^0-9]', bairro):
            print("Erro: O código do bairro deve ser um número de 1 a 31")
            return False
        elif int(bairro) < 1 or int(bairro) > 31:
            print("Erro: O código de bairro não está na lista apresentada")
            return False

        return True

    def Endereco(self, endereco):
        if not endereco or endereco.isspace():
            print("Erro: Endereço não pode ser vazio")
            return False

        return True

    def Area(self, area):
        if not area or area.isspace():
            print("Erro: Area não pode ser vazio")
            return False
        elif re.search(r'[^0-9]', area):
            print("Erro: O código da area deve ser um número de 1 a 7")
            return False
        elif int(area) < 1 or int(area) > 7:
            print("Erro: O código de area não está na lista apresentada")
            return False

        return True

    def Desc(self, desc):
        if len(desc) > 100:
            return desc[0:100]

        return desc

    def Senha(self, senha, conf_senha):
        if not senha or senha.isspace():
            print("Erro: Senha não pode ser vazia")
            return False
        elif conf_senha != senha:
            print("Erro: Senhas diferentes")
            return False
        elif " " in senha:
            print("Erro: Senha não pode ter espaços em branco")
            return False
        elif len(senha) < 5 or len(senha) > 11:
            print("Erro: Senha precisa ter entre 5 a 11 digitos")
            return False


        return True
