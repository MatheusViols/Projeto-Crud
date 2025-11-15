from CRUD.Usuarios.Usuario import Usuario

import mysql.connector

class Read:
    def __init__(self, cnx, cursor):
        self.__cnx = cnx
        self.__cursor = cursor

    def usuarioExiste(self, login):
        self.__cursor.execute(f"SELECT login FROM usuario WHERE login = '{login}';")
        fetch_login = self.__cursor.fetchone()

        if fetch_login and login == fetch_login[0]: 
            return fetch_login[0]

        return False

    def validaUsuario(self, usuario, senha):
        self.__cursor.execute(f"SELECT senha FROM usuario WHERE login = '{usuario}';")
        fetch_senha = self.__cursor.fetchone()

        if fetch_senha:
            return senha ==  fetch_senha[0] 

        return False



    def mostraUsuario(self, login, senha):
        usuario = self.usuarioExiste(login)
        if usuario and self.validaUsuario(usuario, senha):
            self.__cursor.execute(f"SELECT login, nome, sobrenome, endereco FROM usuario WHERE login = '{login}';")
            fetch_info = self.__cursor.fetchone()

            print(f"""
                Login: {fetch_info[0]}
                Nome completo: {fetch_info[1]} {fetch_info[2]}
                Endereço: {fetch_info[3]}
            """)
            return True

        return False





        

