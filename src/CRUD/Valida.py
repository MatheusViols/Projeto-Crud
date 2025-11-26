import re

import datetime
from datetime import date

import mysql.connector

class Valida:
    def __init__(self, chave):
        self.__cnx = chave.cnx
        self.__cursor = chave.cursor

    def campoVazio(self, campo):
        if not campo or campo.isspace():
            print("Erro: Esse campo não pode ser vazio")
            return True
        return False

    def naoNumero(self, campo):
        if re.search(r'[^0-9]', campo):
            print("Erro: Esse campo aceita apenas números")
            return True
        return False

    def temEspaco(self, string):
        if " " in string:
            print("Erro: Esse campo não aceita uso de espaços")
            return True
        return False

    def diferente(self, tamanho, tamanho_fixo):
        if tamanho != tamanho_fixo:
            print(f"Erro: Esse campo tem um tamanho fixo de {tamanho_fixo}")
            return True
        return False

    def foraDe(self, valor, minimo, maximo):
        if valor < minimo or valor > maximo:
            print(f"Erro: Esse campo só aceita valores entre {minimo} e {maximo}")
            return True
        return False
                

    def chaveExiste(self, chave, tabela, valor):
        self.__cursor.execute(f"SELECT {chave} FROM {tabela} WHERE {chave} = '{valor}'")
        chave = self.__cursor.fetchone()
        if chave and chave[0] == valor:
            return True

        return False

    def CPF(self, CPF):
        if self.campoVazio(CPF):
            return False
        elif self.naoNumero(CPF):
            return False
        elif self.diferente(len(CPF),11):
            return False

        return True



    def CNPJ(self, CNPJ):
        if self.campoVazio(CNPJ):
            return False
        elif self.naoNumero(CNPJ):
            return False
        elif self.diferente(len(CNPJ),14):
            return False

        return True


    def Nome(self, nome_comp):
        if self.campoVazio(nome_comp):
            return False

        return True

    def Data(self, dia, mes, ano):
        if self.campoVazio(dia) or self.campoVazio(mes) or self.campoVazio(ano):
            return False
        elif self.naoNumero(dia) or self.naoNumero(mes) or self.naoNumero(ano):
            return False
        elif self.diferente(len(dia),2) or self.diferente(len(mes),2) or self.diferente(len(ano),4):
            return False

        try:
            datetime.datetime(year=int(ano), month=int(mes), day=int(dia))
        except ValueError:
            print("Erro: Data inválida")
            return False

        ano_atual = int(date.today().year)
        ano = int(ano)
        if (ano_atual - ano) not in range(18, 30):
            print("Erro: O programa é destinado apenas aos jovens entre 18 a 29 anos")
            return False


        return True

    def Telefone(self, telefone):
        if self.campoVazio(telefone):
            return False
        elif self.naoNumero(telefone):
            return False
        elif self.diferente(len(telefone),11):
            return False

        return True



    def Bairro(self, cod_bairro):
        if self.campoVazio(cod_bairro):
            return False
        elif self.naoNumero(cod_bairro):
            return False
        elif self.foraDe(int(cod_bairro), 1, 31):
            return False

        return True

    def Endereco(self, endereco):
        if self.campoVazio(endereco):
            return False

        return True

    def Area(self, cod_area):
        if self.campoVazio(cod_area):
            return False
        elif self.naoNumero(cod_area):
            return False
        elif self.foraDe(int(cod_area), 1, 8):
            return False

        return True

    def Desc(self, desc):
        if len(desc) > 100:
            return False
        return True

    def Senha(self, senha, conf_senha):
        if self.campoVazio(senha) or self.campoVazio(conf_senha):
            return False
        elif conf_senha != senha:
            print("Erro: Senhas diferentes")
            return False
        elif self.temEspaco(senha):
            return False
        elif self.foraDe(len(senha), 5, 12):
            return False

        return True

    def nomeCurso(self, nome_comp):
        if self.campoVazio(nome_comp):
            return False

        return True

    def nomeVaga(self, nome_comp):
        if self.campoVazio(nome_comp):
            return False

        return True

    def Turno(self, cod_turno):
        if self.campoVazio(cod_turno):
            return False
        elif self.naoNumero(cod_turno):
            return False
        elif self.foraDe(int(cod_turno), 1, 3):
            return False

        return True
