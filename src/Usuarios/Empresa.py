from CRUD.Create import Create
from CRUD.Read import Read
from CRUD.Valida import Valida
from CRUD.Update import Update

from Dados import *

class Empresa:
    def __init__(self, dados, chave):
        self.__dados = dados
        self.__chave = chave

        self.__vagas = None
        self.VAGA_ATRIBUTOS = "cod_vaga, nome_vaga, quant_vagas, desc_vaga, cod_area, cod_turno"

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
        if not self.__vagas:
            print("Nenhuma vaga cadastrada")
            return
        for vaga in self.__vagas:
            print(f"""
                codigo: {vaga[0]}
                nome: {vaga[1]}
                vagas: {vaga[2]}
                codigo de área: {vaga[4]}
                codigo de turno: {vaga[5]}

                descrição: {vaga[3]}
            """)

    def atualizaVagas(self):
        buscar = Read(self.__chave)
        self.__vagas = buscar.selectAllWhere(self.VAGA_ATRIBUTOS, 'vaga', f"CNPJ = '{self.__dados.CNPJ}'")

    def cadastrarVaga(self):
        cadastro = Create(self.__chave)

        if not cadastro.cadVaga(self.__dados.CNPJ, self.__dados.cod_bairro):
            return False

        return True if self.atualizaVagas() else False

    def atualizarDados(self):
        while True:
            dicio_dados = {
                    '1':'nome_emp',
                    '2':'endereco',
                    '3':'desc_emp',
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
            atualizar.updateWhere('empresa',
                                  dicio_dados[codigo_dado],
                                  f"'{valor.dado}'",
                                  f"CNPJ = '{self.__dados.CNPJ}' AND senha = '{self.__dados.senha}'")

            buscar = Read(self.__chave)
            select = buscar.selectOneWhere('e.*, nome_bairro',
                                           'empresa e, bairro b',
                                           f"CNPJ = '{self.__dados.CNPJ}' AND e.cod_bairro = b.cod_bairro")

            self.__dados = DadosEmpresa(select)



                                      







