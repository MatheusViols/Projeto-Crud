from CRUD.Create import Create
from CRUD.Read import Read

from Login import Login
from Mensagens import mensagens
from Dados import *

import mysql.connector
import os


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

        elif conf_login == 'sair':
            return
        elif conf_login != "sim":
            print("Por favor, digite apenas sim ou não")
            continue

        return True

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
    if not telaInicial():
        return

    Usuario = logar()


    while True:
        chave = Chave()

        dicio_comandos = {
            'Jovem':mensagens.COMANDOS_JOVEM,
            'Empresa':mensagens.COMANDOS_EMP,
            'Instituição':mensagens.COMANDOS_INST                    
            }

        comandos = dicio_comandos[Usuario.tipo]
        print()
        for codigo in comandos:
            print(f"{codigo} - {comandos[codigo]}")
        print()



        uso = input("Digite o código do comando: ")
        if uso == 'sair': return
        
        if uso not in comandos:
            print("Comando não encontrado")
            continue


        LIMPAR = 'cls' if os.name == 'nt' else 'clear'
        os.system(LIMPAR)

        if Usuario.tipo == 'Jovem':
            match uso:
                case '1': Usuario.info()
                case '2': Usuario.verVagas()
                case '3': Usuario.verAplicacoes()
                case '4': Usuario.aplicarVaga()
                case '5': Usuario.removerAplicacao()
                case '6': Usuario.verCursos()
                case '7': Usuario.verMatriculas()
                case '8': Usuario.matricularCurso()
                case '9': Usuario.removerMatricula()
                case '10': Usuario.atualizarDados()
                case '11': 
                    if Usuario.deletarConta():
                        print("Adeus!")
                        return
                case _: print("Comando não encontrado")
        elif Usuario.tipo == 'Empresa':
            match uso:
                case '1': Usuario.info()
                case '2': Usuario.mostrarVagas()
                case '3': Usuario.cadastrarVaga()
                case '4': Usuario.atualizarDados()
                case '5': 
                    if Usuario.deletarConta():
                        print("Adeus!")
                        return
                case _: print("Comando não encontrado")
        elif Usuario.tipo == 'Instituição':
            match uso:
                case '1': Usuario.info()
                case '2': Usuario.mostrarCursos()
                case '3': Usuario.cadastrarCurso()
                case '4': Usuario.atualizarDados()
                case '5': 
                    if Usuario.deletarConta():
                        print("Adeus!")
                        return
                case _: print("Comando não encontrado")

        input_continuar = input("Digite enter para continuar")
        if input_continuar == 'sair': return

        chave.cursor.close()
        chave.cnx.close()







                



if __name__ == '__main__':
    main()
