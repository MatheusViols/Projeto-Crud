from CRUD.Usuarios.Usuario import Usuario

import mysql.connector

class Create:
    # Recebe a conexão e o cursor na inicialização
    def __init__(self, cnx, cursor):
        self.__cnx = cnx
        self.__cursor = cursor

    def validaLogin(self, login):
        """
        Seleciona linhas em que o login aparece
        fetchone() retorna uma unica linha
        fetchall() retorna todas as linhas encontradas
        Os dois retornam tuplas, fetchone uma tupla que representa uma linha, fetchall
        uma lista de tuplas que representam varias linhas

        Usei fetchone(), por padrão não vai existir mais de uma linha com mesmo login 
        """
        self.__cursor.execute(f"SELECT login FROM usuario WHERE login = '{login}'")
        fetch_login = self.__cursor.fetchone()

        # Comparando o retorno da busca por só por segurança
        if fetch_login and login == fetch_login[0]:
            print("Erro: Login já utilizado")
            return False

        return True

    def validaSenha(self, senha):
        if not senha or senha.isspace():
            print("Erro: Senha não pode ser vazia")
            return False


        confSenha = input("Confirme a senha: ")
        if confSenha != senha:
            print("Erro: Senhas diferentes")
            return False

        if " " in senha:
            print("Erro: Senha não pode ter espaços em branco")
            return False

        return True

    def validaNome(self, nome):
        if not nome or nome.isspace():
            print("Erro: Nome não pode ser vazio")
            return False

        if " " in nome:
            print("Erro: Sem espaços em branco, apenas o primeiro nome")
            return False

        return True

    def validaSobrenome(self, sobrenome):
        if not sobrenome or sobrenome.isspace():
            print("Erro: Sobrenome não pode ser vazio")
            return False

        if " " in sobrenome:
            print("Erro: Sem espaços em branco, apenas o sobrenome")
            return False

        return True


    def validaEndereco(self, endereco):
        if not endereco or endereco.isspace():
            print("Erro: Endereço não pode ser vazio")
            return False

        return True

    def criarUsuario(self):
        """
        A função vai receber as informações e testar se são válidas.
        Informações inválidas: login que já existe, vazia, composta só de espaços, com
        espaço(exceto endereço), confirmação diferente de valor(por enquanto só em senha)

        Em caso de alguma dessas, retorna False, o tipo de erro e a criação não é finalizada
        """
        login = input("login: ")
        if not self.validaLogin(login): 
            return False

        senha = input("senha: ")
        if not self.validaSenha(senha): 
            return False

        nome = input("nome: ")
        if not self.validaNome(nome):
            return False

        sobrenome = input("sobrenome: ")
        if not self.validaSobrenome(sobrenome):
            return False

        endereco = input("Endereço: ")
        if not self.validaEndereco(endereco):
            return False

        """
        Insere uma nova linha com as informações adiquiridas

        self.__cnx.commit() é importante, as mudanças não vão ser feitas sem ela.
        Depois de um cursor.execute() que insira, delete ou atualize a tabela, sempre
        usar self.__cnx.commit()
        """
        self.__cursor.execute(f"INSERT INTO usuario(login, senha, nome, sobrenome, endereco) VALUES('{login}', '{senha}', '{nome}', '{sobrenome}', '{endereco}')")
        self.__cnx.commit()

        return True





