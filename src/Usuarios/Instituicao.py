from CRUD.Create import Create
from CRUD.Update import Update
from CRUD.Read import Read

import mysql.connector

from Dados import *

class Instituicao:
    def __init__(self, dados, chave):
        self.__dados = dados
        self.__chave = chave
        self.__cnx = chave.cnx
        self.__cursor = chave.cursor

        self.__cursos = None
        self.CURSO_ATRIBUTOS = "cod_curso, nome_curso, quant_vagas, desc_curso, cod_area, cod_turno"

        self.atualizaCursos()

        self.tipo = 'Instituição'

    def info(self):
        print(f"""
                CNPJ: {self.__dados.CNPJ}
                Nome: {self.__dados.nome_inst}
                Endereço: {self.__dados.endereco}
                Descrição: {self.__dados.desc_inst}

                Bairro: {self.__dados.nome_bairro} | Codigo {self.__dados.cod_bairro} 

        """)

    def mostrarCursos(self):
        if not self.__cursos:
            print("Nenhum curso cadastrado")
            return 
        for curso in self.__cursos:
            print(f"""
                codigo: {curso[0]}
                nome: {curso[1]}
                vagas: {curso[2]}
                codigo de área: {curso[4]}
                codigo de turno: {curso[5]}

                descrição: {curso[3]}
            """)
                


    def atualizaCursos(self):
        try:
            self.__cursor.execute(f"SELECT {self.CURSO_ATRIBUTOS} FROM curso WHERE CNPJ = '{self.__dados.CNPJ}'")
            self.__cursos = self.__cursor.fetchall()
            return True
        except mysql.connector.errors.DatabaseError:
            print("Algo deu errado durante a atualização de cursos, atualização não finalizada")
            return False
        

    def cadastrarCurso(self):
        cadastro = Create(self.__chave)

        if not cadastro.cadCurso(self.__dados.CNPJ, self.__dados.cod_bairro):
            return False

        return (True if self.atualizaCursos() else False)


    def atualizarDados(self):
        while True:
            dicio_dados = {
                    '1':'nome_inst',
                    '2':'endereco',
                    '3':'desc_inst',
                    '4':'cod_bairro'
                    }
            for dado in dicio_dados:
                print(f"{dado} - {dicio_dados[dado]}")
            codigo_dado = input("Digite o código do dado que deseja atualizar: ")
            if not codigo_dado or codigo_dado not in dicio_dados: return False

            match codigo_dado:
                case '1': valor = InputValido('Digite seu novo nome', 'nome')
                case '2': valor = InputValido('Digite seu novo endereço', 'endereco')
                case '3': valor = InputValido('Digite sua nova descrição', 'descricao')
                case '4': valor = InputValido('Digite o codigo de bairro', 'bairro')
                case 'sair': break
                case _:
                    print("Código de dado não encontrado")
                    continue

            atualizar = Update(self.__chave)
            atualizar.updateWhere('instituicao',
                                  dicio_dados[codigo_dado],
                                  f"'{valor.dado}'",
                                  f"CNPJ = '{self.__dados.CNPJ}' AND senha = '{self.__dados.senha}'")

            buscar = Read(self.__chave)
            select = buscar.selectOneWhere('i.*, nome_bairro',
                                           'instituicao i, bairro b',
                                           f"CNPJ = '{self.__dados.CNPJ}' AND i.cod_bairro = b.cod_bairro")

            self.__dados = DadosInstituicao(select)



