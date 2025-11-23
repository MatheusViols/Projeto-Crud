from CRUD.Create import Create
from CRUD.Read import Read

class Jovem:
    def __init__(self, atts, area, bairro):
        self.__CPF = atts[0]
        self.__senha = atts[1]
        self.__nome_comp = atts[2]
        self.__data_nasc = atts[3]
        self.__telefone = atts[4]
        self.__endereco = atts[5]
        self.__desc = atts[6]

        self.__cod_area = atts[7]
        self.__cod_bairro = atts[8]

        self.__nome_area = area 
        self.__nome_bairro = bairro 

        self.__aplicacoes = None
        self.__matriculas = None


    def info(self):
        print(f"""
                CPF: {self.__CPF}
                Nome: {self.__nome_comp}
                Data de nascimento: {self.__data_nasc}
                Telefone: {self.__telefone}
                Endereço: {self.__endereco}
                Descrição: {self.__desc}

                Área: {self.__nome_area} Codigo: {self.__cod_area}
                Bairro: {self.__nome_bairro} Codigo: {self.__cod_bairro}
        """)


    def verVagas(self, cnx, cursor):
        buscar = Read(cnx, cursor)
        vagas = buscar.selectVagas(self.__cod_area)
        if not vagas:
            print("Nenhuma vaga encontrada")
            return False

        for vaga in vagas:
            print(f"""
                Codigo: {vaga[0]} | Nome: {vaga[1]}
                Empresa: {vaga[5]}
                Área: {vaga[3]}
                Turno: {vaga[4]}
                Bairro: {vaga[6]}
                Vagas: {vaga[2]}

                Descrição: {vaga[7]}
            """)

    def verAplicacoes(self, cnx, cursor):
        for aplicacao in self.__aplicacoes:
            print(f"""
                Nome: {aplicacao[0]}
                Status {'Em espera' if aplicacao[1] == 0 else 'Aprovada'}

            """)



    def aplicarVaga(self, cnx, cursor):
        buscar = Read(cnx, cursor)
        cadastro = Create(cnx, cursor)
        
        cod_vaga = int(input("Código da vaga: "))

        vaga = buscar.selectWhere('cod_vaga', 'vaga', f'cod_vaga = {cod_vaga}')
        if not vaga:
            print("Não foi encontrada uma vaga com esse código")
            return False

        if not cadastro.cadAplicacao(self.__CPF, cod_vaga):
            return False

        self.atualizaAplicacoes(cnx, cursor)

    def atualizaAplicacoes(self, cnx, cursor):
        buscar = Read(cnx, cursor)
        aplicacoes = buscar.selectAplicacoes(self.__CPF)
        if not aplicacoes:
            return False
        self.__aplicacoes = aplicacoes





    def matricularCurso(self):
        pass
