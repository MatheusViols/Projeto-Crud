from CRUD.Usuarios.Usuario import Usuario

import mysql.connector

class Create:
    def __init__(self, cnx, cursor):
        self.__cnx = cnx
        self.__cursor = cursor

    def validaLogin(self, login):
        self.__cursor.execute(f"SELECT login FROM usuario WHERE login = '{login}'")
        fetch_login = self.__cursor.fetchone()

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

        self.__cursor.execute(f"INSERT INTO usuario(login, senha, nome, sobrenome, endereco) VALUES('{login}', '{senha}', '{nome}', '{sobrenome}', '{endereco}')")
        self.__cnx.commit()

        return True





