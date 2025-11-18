import re 
import datetime

class Create:
    def __init__(self):
        pass

    def validaCPF(self, CPF):
        if not CPF:
            return False
        elif re.search(r'[^0-9]', CPF):
            print("Erro: CPF aceita apenas números")
            return False
        elif len(CPF) < 11:
            print("Erro: CPF tem o número fixo de 11 digitos")
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
        



    def cadJovem(self):
        CPF = input("CPF: ")
        if not validaCPF(CPF):
            return False

        nome_comp = input("Nome completo: ")
        if not validaNome(nome_comp):
            return False

        dia = input("Dia de nascimento: ")
        mes = input("Mês de nascimento: ")
        ano = input("Ano de nascimento: ")
        if not validaData(dia, mes, ano):
            return False

        telefone = input("Telefone: ")
        if not validaTelefone(telefone):
            return False





