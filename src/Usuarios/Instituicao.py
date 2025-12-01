from CRUD.Create import Create
from CRUD.Update import Update
from CRUD.Read import Read
from CRUD.Delete import Delete

import mysql.connector

from Dados import *

class Instituicao:
    def __init__(self, dados, chave):
        self.__dados = dados
        self.__chave = chave
        self.__cnx = chave.cnx
        self.__cursor = chave.cursor

        self.__cursos = None

        self.CURSOS_ATRIBUTOS = """
                        cod_curso, nome_curso, quant_vagas, desc_curso, c.cod_area, c.cod_turno, c.cod_bairro,
                        nome_area, nome_turno, nome_inst, nome_bairro
                               """
        self.CURSOS_TABELAS = "curso c, area ar, turno t, instituicao i, bairro b"
        self.CURSOS_FILTRO = f"""
                        c.CNPJ = {self.__dados.CNPJ} AND
                        c.cod_area = ar.cod_area AND
                        c.cod_turno = t.cod_turno AND
                        c.cod_bairro = b.cod_bairro
                              """

                        

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
        if not self.__cursos.dados:
            print("Nenhum curso cadastrado")
            return 
        for curso in self.__cursos.dados:
            print(f"""
                codigo: {curso}
                nome: {self.__cursos.dados[curso]['nome']}
                vagas: {self.__cursos.dados[curso]['quant']}
                Área: {self.__cursos.dados[curso]['nome_area']}
                Turno: {self.__cursos.dados[curso]['nome_turno']}

                descrição: {self.__cursos.dados[curso]['desc']}
            """)
                


    def atualizaCursos(self):
        buscar = Read(self.__chave)
        select = buscar.selectAllWhereERRO(self.CURSOS_ATRIBUTOS, self.CURSOS_TABELAS, self.CURSOS_FILTRO)

        self.__cursos = DadosCursos(select)
        

    def cadastrarCurso(self):
        cadastro = Create(self.__chave)

        if not cadastro.cadCurso(self.__dados.CNPJ, self.__dados.cod_bairro):
            return False

        return (True if self.atualizaCursos() else False)

    def removerCurso(self):
        try:
            input_cod_curso = int(input("Digite o código do curso  que quer remover: "))
        except ValueError:
            if input_cod_curso == 'sair': 
                return False
            else:
                print("Esse campo aceita apenas inteiros")
                return False

        remover = Delete(self.__chave)
        if not remover.deleteWhere('curso', f"CNPJ = '{self.__dados.CNPJ}' AND cod_curso = {input_cod_curso}"):
            print("Código de curso não encontrado")
            return False

        self.atualizaCursos()
        return True

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
            if codigo_dado == 'sair': 
                return False
            if not codigo_dado or codigo_dado not in dicio_dados: 
                print("Código de dado não encontrado")
                return False

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

    def deletarConta(self):
        print("Você tem total certeza de que deseja deletar sua conta?")
        confirmacao = input("-> ").lower()

        if confirmacao == 'sim':
            input_senha = input("Digite a sua senha: ")
            conf_input_senha = input("Confirme sua senha: ")

            if (input_senha and conf_input_senha) and (input_senha == conf_input_senha) and (input_senha == self.__dados.senha):
                deletar = Delete(Chave())
                deletar.deleteWhere('instituicao', f"CNPJ = '{self.__dados.CNPJ}'")

                return True
            else:
                print("Senha incorreta")
                return False

        else:
            return False


