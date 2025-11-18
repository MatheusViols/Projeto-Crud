class Instituicao:
    def __init__(self, atts, bairro):
        self.__CNPJ = atts[0]
        self.__senha = atts[1]
        self.__nomeEmp = atts[2]
        self.__endereco = atts[3]
        self.__desc = atts[4]

        self.__bairro = bairro 

    def info(self):
        print(f"""
                CNPJ: {self.__CNPJ}
                Nome: {self.__nomeEmp}
                Endereço: {self.__endereco}
                Descrição: {self.__desc}
                Bairro: {self.__bairro}
        """)

    def buscarVagas(self):
        pass

    def aplicarVaga(self):
        pass

    def removerAplicacao(self):
        pass

    def statusAplicacao(self):
        pass




    def buscarCursos(self):
        pass

    def matricularCurso(self):
        pass

    def removerMatricula(self):
        pass

    def statusMatricula(self):
        pass




    def alterarDados(self):
        pass

    def mapa(self):
        pass

