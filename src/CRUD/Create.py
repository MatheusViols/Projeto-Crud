import re 
import datetime
from datetime import date

from Mensagens import mensagens
 
import mysql.connector

class Create:
    def __init__(self, cnx, cursor):
        self.__cnx = cnx
        self.__cursor = cursor

    def validaCPF(self, CPF):
        if not CPF:
            return False
        elif re.search(r'[^0-9]', CPF):
            print("Erro: CPF aceita apenas números")
            return False
        elif len(CPF) < 11:
            print("Erro: CPF tem o número fixo de 11 digitos")
            return False


        self.__cursor.execute(f"SELECT CPF FROM usuario WHERE CPF = '{CPF}';")
        fetch_CPF = self.__cursor.fetchone()
        if fetch_CPF and fetch_CPF[0] == CPF:
            print("Erro: CPF já está cadastrado")
            return False


        return True

    def validaNome(self, nome_comp):
        if not nome_comp or nome_comp.isspace():
            return False

        return True

    def validaData(self, dia, mes, ano):
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
        
    def validaTelefone(self, telefone):
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
        


    def validaBairro(self, bairro):
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
    
    def validaEndereco(self, endereco):
        if not endereco or endereco.isspace():
            print("Erro: Endereço não pode ser vazio")
            return False

        return True

    def validaArea(self, area):
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

    def validaDesc(self, desc):
        if len(desc) > 100:
            return desc[0:100]

        return desc

    def validaSenha(self, senha, conf_senha):
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
            pritn("Erro: Senha precisa ter entre 5 a 11 digitos")
            return False


        return True




    def cadJovem(self):
        CPF = input("CPF: ")
        if not self.validaCPF(CPF):
            return False

        nome_comp = input("Nome completo: ")
        if not self.validaNome(nome_comp):
            return False

        dia = input("Dia de nascimento: ")
        mes = input("Mês de nascimento: ")
        ano = input("Ano de nascimento: ")
        if not self.validaData(dia, mes, ano):
            return False

        telefone = input("Telefone: ")
        if not self.validaTelefone(telefone):
            return False

        print(mensagens.MSG_COD_BAIRRO)
        bairro = input("Bairro: ") 
        if not self.validaBairro(bairro):
            return False

        endereco = input("Endereço: ")
        if not self.validaEndereco(endereco):
            return False

        print(mensagens.MSG_COD_AREA)
        area = input("Área: ")
        if not self.validaArea(area):
            return False

        print(mensagens.MSG_DESC)
        desc_user = input("Descrição: ")
        desc_user = self.validaDesc(desc_user) 

        print(mensagens.MSG_SENHA)
        senha = input("Senha: ")
        conf_senha = input("Confirme a senha: ")
        if not self.validaSenha(senha, conf_senha):
            return False


        try:
            self.__cursor.execute(f"INSERT INTO usuario(CPF, senha, nome_comp, data_nasc, telefone, endereco, desc_user, cod_area, cod_bairro) VALUES('{CPF}', '{senha}', '{nome_comp}', '{ano}-{mes}-{dia}', '{telefone}', '{endereco}', '{desc_user}', {area}, {bairro});")
            self.__cnx.commit()
            return True
        except mysql.connector.erros.DatabaseError:
            print("Erro: Algo deu errado durante a inserção de dados, cadastro não finalizado")
            return False

        
         

            





