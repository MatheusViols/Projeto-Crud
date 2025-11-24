from CRUD.Create import Create
from CRUD.Read import Read

from Login import Login
from Mensagens import mensagens
import TesteValida

from Dados import *

import mysql.connector


def tipoConta():
    while True:
        try:
            tipo_conta = int(input("     -> "))
        except ValueError:
            print("Por favor, digite apenas números")
            continue

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
                    chave = Chave()
                    cadastro = Create(chave)
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

                    chave.cursor.close()
                    chave.cnx.close()

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

        chave = Chave()
        login = Login(chave)

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

    chave = Chave()
    Usuario.verAplicacoes()
    Usuario.verMatriculas()



if __name__ == '__main__':
    main()
