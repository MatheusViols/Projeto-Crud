from CRUD.Create import Create 
from CRUD.Read import Read

from CRUD.Usuarios.Usuario import Usuario

import mysql.connector

"""
Faz a conexão com o mysql e a database. Retorna uma tupla com o objeto de conexão(indice [0]) e o objeto cursor usado para editar o banco(indice [1])

Decidi não criar a conexão no __init__() dos objetos pra garantir que a conexão seja fechada, mesmo em casos que a operação não termine, sem precisar adicionar cursor.close() e cnx.close() no final de todos os métodos. Isso poderia fechar a conexão antes de criar.criarUsuario() terminar.

Ainda não sei se seria melhor criar a conexão só uma vez e usar ela durante a execução inteira do programa ou conectar ela só quando necessário, por desconfiança escolhi a segunda opção.
"""
def conexao():
    cnx = mysql.connector.connect(user='crud-user', password='crud-user', host='localhost', database='crud') 
    cursor = cnx.cursor()

    return cnx, cursor



# Loop simples pra receber o tipo de operação e escolher o caminho
while True:
    uso = input("[ CRUD ] $ ")

    if uso == 'create':
        banco = conexao()

        criar = Create(banco[0], banco[1])

        usuario = criar.criarUsuario()

        """
        Até agora todos os métodos retornam False em caso de erro e True caso finalize sem 
        problemas. Caso algum método no futuro retorne algum dado, a mesma estrutura condi
        cional deve funcionar sem problemas.
        """
        if usuario:
            print("\nUsuario cadastrado com sucesso\n")
        else:
            print("\nNão foi possivel criar o usuario\n")

        """
        Lembrar de sempre fechar as conexões, não fazer isso pode trancar o banco
        Talvez isso ainda aconteça se o programa finalizar cedo com algum erro, vou tentar
        consertar isso
        """
        banco[1].close()
        banco[0].close()

    elif uso == 'show':
        login = input("login: ")
        senha = input("senha: ")


        banco = conexao()

        ler = Read(banco[0], banco[1])
        if not ler.mostraUsuario(login, senha):
            print(f"Erro: {login} não encontrado")


        banco[1].close()
        banco[0].close()
    elif uso == 'sair':
        # Sai do loop 
        break
    else:
        print(f"Comando {uso} não faz parte do conjunto de comandos padrão")








