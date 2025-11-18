from CRUD.Valida import Valida
from Usuarios.Jovem import Jovem
from Usuarios.Empresa import Empresa
from Usuarios.Instituicao import Instituicao

class Login:
    def __init__(self, cnx, cursor):
        self.__cnx = cnx
        self.__cursor = cursor
        self.__validar = Valida(cnx, cursor)


    def logarJovem(self):
        CPF = input("CPF: ")
        if not self.__validar.CPF(CPF):
            return False
        senha = input("Senha: ")
        conf_senha = input("Confirme a senha: ")
        if not self.__validar.Senha(senha, conf_senha):
            return False

        if self.__validar.CPFExiste(CPF):
            self.__cursor.execute(f"SELECT senha FROM usuario WHERE CPF = '{CPF}';")
            fetch_senha = self.__cursor.fetchone()
            if fetch_senha and fetch_senha[0] == senha:
                self.__cursor.execute(f"SELECT * FROM usuario WHERE CPF = '{CPF}';")
                fetch_user = self.__cursor.fetchone()

                self.__cursor.execute(f"SELECT nome_area FROM area WHERE cod_area = '{fetch_user[7]}';")
                fetch_area = self.__cursor.fetchone()

                self.__cursor.execute(f"SELECT nome_bairro FROM bairro WHERE cod_bairro = '{fetch_user[8]}';")
                fetch_bairro = self.__cursor.fetchone()
                return Jovem(fetch_user, fetch_area[0], fetch_bairro[0])

        return False



    def logarEmpresa(self):
        CNPJ = input("CNPJ: ")
        if not self.__validar.CNPJ(CNPJ):
            return False
        senha = input("Senha: ")
        conf_senha = input("Confirme a senha: ")
        if not self.__validar.Senha(senha, conf_senha):
            return False

        if self.__validar.CNPJEmpExiste(CNPJ):
            self.__cursor.execute(f"SELECT senha FROM empresa WHERE CNPJ = '{CNPJ}';")
            fetch_senha = self.__cursor.fetchone()
            if fetch_senha and fetch_senha[0] == senha:
                self.__cursor.execute(f"SELECT * FROM empresa WHERE CNPJ = '{CNPJ}';")
                fetch_user = self.__cursor.fetchone()

                self.__cursor.execute(f"SELECT nome_bairro FROM bairro WHERE cod_bairro = '{fetch_user[5]}';")
                fetch_bairro = self.__cursor.fetchone()
                return Empresa(fetch_user, fetch_bairro[0])

        return False

    def logarInstituicao(self):
        CNPJ = input("CNPJ: ")
        if not self.__validar.CNPJ(CNPJ):
            return False
        senha = input("Senha: ")
        conf_senha = input("Confirme a senha: ")
        if not self.__validar.Senha(senha, conf_senha):
            return False

        if self.__validar.CNPJInstExiste(CNPJ):
            self.__cursor.execute(f"SELECT senha FROM instituicao WHERE CNPJ = '{CNPJ}';")
            fetch_senha = self.__cursor.fetchone()
            if fetch_senha and fetch_senha[0] == senha:
                self.__cursor.execute(f"SELECT * FROM instituicao WHERE CNPJ = '{CNPJ}';")
                fetch_user = self.__cursor.fetchone()

                self.__cursor.execute(f"SELECT nome_bairro FROM bairro WHERE cod_bairro = '{fetch_user[5]}';")
                fetch_bairro = self.__cursor.fetchone()
                return Instituicao(fetch_user, fetch_bairro[0])

        return False
    

