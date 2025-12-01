from CRUD.Create import Create
from CRUD.Read import Read
from CRUD.Valida import Valida
from CRUD.Update import Update
from CRUD.Delete import Delete

from Dados import *

class Empresa:
    def __init__(self, dados, chave):
        self.__dados = dados
        self.__chave = chave

        self.__vagas = None
        self.VAGAS_ATRIBUTOS = """
                            cod_vaga, nome_vaga, quant_vagas, desc_vaga, v.cod_area, v.cod_turno, v.cod_bairro,
                            nome_area, nome_turno, nome_emp, nome_bairro
                              """
        self.VAGAS_TABELAS = "vaga v, area ar, turno t, bairro b, empresa e"
        self.VAGAS_FILTRO = f"""
                            v.CNPJ = {self.__dados.CNPJ} AND
                            v.cod_area = ar.cod_area AND
                            v.cod_turno = t.cod_turno AND
                            v.cod_bairro = b.cod_bairro
                            """

        self.atualizaVagas()

        self.tipo = 'Empresa'

    def info(self):
        print(f"""
                CNPJ: {self.__dados.CNPJ}
                Nome: {self.__dados.nome_emp}
                Endereço: {self.__dados.endereco}
                Descrição: {self.__dados.desc_emp}

                Bairro: {self.__dados.nome_bairro}  |  codigo: {self.__dados.cod_bairro}
        """)

    def mostrarVagas(self):
        if not self.__vagas.dados:
            print("Nenhuma vaga cadastrada")
            return
        for vaga in self.__vagas.dados:
            print(f"""
                codigo: {vaga}
                nome: {self.__vagas.dados[vaga]['nome']}
                vagas: {self.__vagas.dados[vaga]['quant']}
                Área: {self.__vagas.dados[vaga]['nome_area']}
                Turno: {self.__vagas.dados[vaga]['nome_turno']}

                descrição: {self.__vagas.dados[vaga]['desc']}
            """)

    def atualizaVagas(self):
        buscar = Read(self.__chave)
        select = buscar.selectAllWhereERRO(self.VAGAS_ATRIBUTOS, self.VAGAS_TABELAS, self.VAGAS_FILTRO)
        self.__vagas = DadosVagas(select)

    def cadastrarVaga(self):
        cadastro = Create(self.__chave)

        if not cadastro.cadVaga(self.__dados.CNPJ, self.__dados.cod_bairro):
            return False

        return True if self.atualizaVagas() else False

    def removerVaga(self):
        try:
            input_cod_vaga = int(input("Digite o código da vaga que quer remover: "))
        except ValueError:
            if input_cod_vaga == 'sair': 
                return False
            else:
                print("Esse campo aceita apenas inteiros")
                return False

        remover = Delete(self.__chave)
        if not remover.deleteWhere('vaga', f"CNPJ = '{self.__dados.CNPJ}' AND cod_vaga = {input_cod_vaga}"):
            print("Código de vaga não encontrado")
            return False

        self.atualizaVagas()
        return True



    def atualizarDados(self):
        while True:
            dicio_dados = {
                    '1':('nome_emp', lambda: InputValido('Digite seu novo nome', 'nome')),
                    '2':('endereco', lambda: InputValido('Digite seu novo endereço', 'endereco')),
                    '3':('desc_emp', lambda: InputValido('Digite sua nova descrição', 'descricao')),
                    '4':('cod_bairro', lambda: InputValido('Digite o código de bairro', 'bairro'))
                    }

            for dado in dicio_dados:
                print(f"{dado} - {dicio_dados[dado][0]}")

            codigo_dado = input("Digite o código do dado que deseja atualizar: ")
            if codigo_dado == 'sair':
                return 
            elif not codigo_dado or codigo_dado not in dicio_dados: 
                print("Código de dado não encontrado")
                continue 

            ATRIBUTO = dicio_dados[codigo_dado][0]
            INPUT_VALOR = dicio_dados[codigo_dado][1]
            VALOR = INPUT_VALOR() 

            atualizar = Update(self.__chave) 
            atualizar.updateWhere('empresa',
                                  ATRIBUTO,
                                  f"'{VALOR.dado}'",
                                  f"CNPJ = '{self.__dados.CNPJ}' AND senha = '{self.__dados.senha}'")

            buscar = Read(self.__chave)
            select = buscar.selectOneWhere('e.*, nome_bairro',
                                           'empresa e, bairro b',
                                           f"CNPJ = '{self.__dados.CNPJ}' AND e.cod_bairro = b.cod_bairro")

            self.__dados = DadosEmpresa(select)

    def deletarConta(self):
        print("Você tem total certeza de que deseja deletar sua conta?")
        confirmacao = input("-> ").lower()

        if confirmacao == 'sim':
            input_senha = input("Digite a sua senha: ")
            conf_input_senha = input("Confirme sua senha: ")

            if (input_senha and conf_input_senha) and (input_senha == conf_input_senha) and (input_senha == self.__dados.senha):
                deletar = Delete(Chave())
                deletar.deleteWhere('empresa', f"CNPJ = '{self.__dados.CNPJ}'")

                return True
            else:
                print("Senha incorreta")
                return False

        else:
            return False




                                      







