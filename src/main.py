from CRUD.Create import Create
from CRUD.Read import Read

from Login import Login

from Mensagens import mensagens

import mysql.connector




def conexao():
    cnx = mysql.connector.connect(user='crud-user', password='crud-user', host='localhost', database='crud') 
    cursor = cnx.cursor()

    return cnx, cursor

def tipoConta():
    while True:
        tipo_conta = int(input("     -> "))

        if tipo_conta not in range(1, 4):
            print(f"\nErro: {tipo_conta} não é uma opção\n")
            continue

        return tipo_conta


def telaInicial():
    while True:
        print(mensagens.MSG_INICIAL)
        conf_login = input("     ->").lower()
        if conf_login == "não":
            while True:
                    banco = conexao()
                    cadastro = Create(banco[0], banco[1])
                    print(mensagens.MSG_TIPO_CAD)
                    tipo = tipoConta()
                    erro = False

                    if tipo == 1:
                        print(mensagens.MSG_CAD_JOVEM)
                        erro = True if not cadastro.cadJovem() else False
                    elif tipo == 2:
                        print(mensagens.MSG_CAD_EMP)
                        erro = True if not cadastro.cadEmpresa() else False
                    elif tipo == 3:
                        print(mensagens.MSG_CAD_INST)
                        erro = True if not cadastro.cadInstituicao() else False

                    banco[1].close()
                    banco[0].close()

                    if erro == False:
                        print("Cadastro criado com sucesso!")
                        break
                    else:
                        print("Não foi possivel completar o cadastro")
                        continue

        elif conf_login != "sim":
            print("Por favor, digite apenas sim ou não")
            continue

        return

def logar():
    while True:
        print(mensagens.MSG_TIPO_LOGIN)
        tipo = tipoConta()
        Usuario = False

        banco = conexao()
        login = Login(banco[0], banco[1])

        if tipo == 1:
            Usuario = login.logarJovem()
        elif tipo == 2:
            Usuario = login.logarEmpresa()
        elif tipo == 3:
            Usuario = login.logarInstituicao()

        if not Usuario:
            print("Erro: Não foi possível logar")
            continue

        return Usuario


def main():
    telaInicial()
    Usuario = logar()
    Usuario.info()


if __name__ == '__main__':
    main()
