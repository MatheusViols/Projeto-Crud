from CRUD.Create import Create
from CRUD.Read import Read

from CRUD.Usuarios.Usuario import Usuario

from Mensagens import mensagens

import mysql.connector




def conexao():
    cnx = mysql.connector.connect(user='crud-user', password='crud-user', host='localhost', database='crud') 
    cursor = cnx.cursor()

    return cnx, cursor

def tipoConta():
    while True:
        print(mensagens.MSG_TIPO_CAD)
        tipo_conta = int(input("     -> "))

        if tipo_conta not in range(1, 3):
            print(f"\nErro: {tipo_conta} não é uma opção\n")
            continue

        return tipo_conta



while True:
    print(mensagens.MSG_INICIAL)

    while True:
        conf_login = input("     ->")

        if conf_login == "Não":
            banco = conexao()
            cadastro = Create(banco[0], banco[1])
            tipo = tipoConta()

            if tipo == 1:
                print(mensagens.MSG_CAD_JOVEM)

                if not cadastro.cadJovem():
                    print("Não foi possivel criar o usuario")
            elif tipo == 2:
                cadastro.cadEmpresa()
            elif tipo == 3:
                cadastro.cadInstituicao()


            print("Cadastro criado com sucesso!")




            
        elif conf_login != "Sim":
            print("Por favor, digite apenas sim ou não")
            continue

"""

# Loop simples pra receber o tipo de operação e escolher o caminho
while True:
    uso = input("[ CRUD ] $ ")

    if uso == 'create':
        banco = conexao()

        criar = Create(banco[0], banco[1])

        usuario = criar.criarUsuario()

        Até agora todos os métodos retornam False em caso de erro e True caso finalize sem 
        problemas. Caso algum método no futuro retorne algum dado, a mesma estrutura condi
        cional deve funcionar sem problemas.

        if usuario:
            print("\nUsuario cadastrado com sucesso\n")
        else:
            print("\nNão foi possivel criar o usuario\n")

        Lembrar de sempre fechar as conexões, não fazer isso pode trancar o banco
        Talvez isso ainda aconteça se o programa finalizar cedo com algum erro, vou tentar
        consertar isso

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







"""
