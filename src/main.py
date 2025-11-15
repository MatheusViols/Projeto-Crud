from CRUD.Create import Create 
from CRUD.Read import Read

from CRUD.Usuarios.Usuario import Usuario

import mysql.connector

# Evite mexer nessa função, tudo é padrão, dificilmente precisa mudar
def conexao():
    cnx = mysql.connector.connect(user='crud-user', password='crud-user', host='localhost', database='crud') 
    cursor = cnx.cursor()

    return cnx, cursor



while True:
    uso = input("[ CRUD ] $ ")

    if uso == 'create':
        banco = conexao()

        criar = Create(banco[0], banco[1])

        usuario = criar.criarUsuario()

        if usuario:
            print("\nUsuario cadastrado com sucesso\n")
        else:
            print("\nNão foi possivel criar o usuario\n")

        banco[1].close()
        banco[0].close()

    elif uso == 'show':
        login = input("login: ")
        senha = input("senha: ")


        banco = conexao()

        ler = Read(banco[0], banco[1])
        ler.mostraUsuario(login, senha)

        banco[1].close()
        banco[0].close()
    elif uso == 'sair':
        break
    else:
        print(f"Comando {uso} não faz parte do conjunto de comandos padrão")








