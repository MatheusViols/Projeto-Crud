from dataclasses import dataclass
from CRUD.Valida import Valida

from Dados import *

import mysql.connector
import os

chave = Chave()
validar = Valida(chave)

MOSTRAR_MSG_ERRO = False
COMANDO_CLEAR = 'cls' if os.name=='nt' else 'clear' 

vazios = (
    validar.CPF(""),
    validar.CNPJ(""),
    validar.Nome(""),
    validar.Telefone(""),
    validar.Bairro(""),
    validar.Data("", "", ""),
    validar.Endereco(""),
    validar.Area(""),
    validar.Senha("", "")
)


naoNumerais = (
        validar.CPF("123sabrina456"),
        validar.CNPJ("123sabrina456"),
        validar.Telefone("123sabrina456"),
        validar.Bairro("123sabrina456"),
        validar.Data("123sabrina456", "123sabrina456", "123sabrina456"),
        validar.Area("123sabrina456")
)


comEspaco = ( 
validar.Senha("mike tyson", "mike tyson"),
validar.Senha("mike tyson", "mike tyson")
)


quantDigitos = (
        validar.CPF('123456789'),
        validar.CPF('123456789123456'),
        validar.CNPJ('123456789'),
        validar.CNPJ('123456789123456'),
        validar.Telefone('81982229'),
        validar.Telefone('81982229999999'),
        validar.Data('1', '2', '223'),
        validar.Data('123', '123', '20256')
)

print()
def buscaErro(lista, tipo_teste):
    cont = 0
    for erro in lista:
        cont += 1
        if erro == True:
            print(f"Erro: {tipo_teste}  Teste Nº{cont}")
    print(f"{tipo_teste}: Validação segura")

if not MOSTRAR_MSG_ERRO: 
    os.system(COMANDO_CLEAR)

buscaErro(vazios, "Inserção de campos vazios")
buscaErro(naoNumerais, "Inserção de não numerais")
buscaErro(comEspaco, "Inserção de espaço")
buscaErro(quantDigitos, "Inserção de tamanhos não esperados")



