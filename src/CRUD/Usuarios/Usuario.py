class Usuario:
    def __init__(self, login, senha, nome, sobrenome, endereco):
        self.__login = login
        self.__senha = senha
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__endereco = endereco

    @property
    def login(self):
        return self.__login

    @property
    def senha(self):
        return self.__senha

    @property
    def nome(self):
        return self.__nome

    @property
    def sobrenome(self):
        return self.__sobrenome

    @property
    def endereco(self):
        return self.__endereco

    


    @login.setter
    def login(self, login):
        self.__login = login

    @senha.setter
    def senha(self, novaSenha):
        self.__senha = novaSenha

    @nome.setter
    def nome(self, novoNome):
        self.__nome = novoNome

    @sobrenome.setter
    def sobrenome(self, novoSobrenome):
        self.__sobrenome = novoSobrenome

    @endereco.setter
    def endereco(self, novoEndereco):
        self.__endereco = novoEndereco
