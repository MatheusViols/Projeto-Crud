class Jovem:
    def __init__(self, atts, area, bairro):
        self.__CPF = atts[0]
        self.__senha = atts[1]
        self.__nomeComp = atts[2]
        self.__dataNasc = atts[3]
        self.__telefone = atts[4]
        self.__endereco = atts[5]
        self.__desc = atts[6]

        self.__area = area 
        self.__bairro = bairro 

    def info(self):
        print(f"""
                CPF: {self.__CPF}
                Nome: {self.__nomeComp}
                Data de nascimento: {self.__dataNasc}
                Telefone: {self.__telefone}
                Endereço: {self.__endereco}
                Descrição: {self.__desc}
                Área: {self.__area}
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

