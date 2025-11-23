from CRUD.Valida import Valida
from Usuarios.Jovem import Jovem
from Usuarios.Empresa import Empresa
from Usuarios.Instituicao import Instituicao

from dataclasses import dataclass

class Login:
    def __init__(self, cnx, cursor):
        self.__cnx = cnx
        self.__cursor = cursor
        self.__validar = Valida(cnx, cursor)


    def selectWHERE(self, atributo, tabela, comparativo, valor):
        self.__cursor.execute( f"SELECT {atributo} FROM {tabela} WHERE {comparativo} = '{valor}';")
        return self.__cursor.fetchone()


    def logarJovem(self):
        CPF = input("CPF: ")
        if not self.__validar.CPF(CPF):
            return False

        senha = input("Senha: ")
        conf_senha = input("Confirme a senha: ")
        if not self.__validar.Senha(senha, conf_senha):
            return False

        if self.__validar.chaveExiste('CPF', 'usuario', CPF):
            select_senha = self.selectWHERE('senha', 'usuario', 'CPF', CPF)

            if select_senha and select_senha[0] == senha:
                user = self.selectWHERE('*', 'usuario', 'CPF', CPF)
                area = self.selectWHERE('nome_area', 'area', 'cod_area', user[7])
                bairro = self.selectWHERE('nome_bairro', 'bairro', 'cod_bairro', user[8])

                return Jovem(user, area[0], bairro[0])

        return False



    def logarEmpresa(self):
        CNPJ = input("CNPJ: ")
        if not self.__validar.CNPJ(CNPJ):
            return False

        senha = input("Senha: ")
        conf_senha = input("Confirme a senha: ")
        if not self.__validar.Senha(senha, conf_senha):
            return False

        if self.__validar.chaveExiste('CNPJ', 'empresa', CNPJ):
            select_senha = self.selectWHERE('senha', 'empresa', 'CNPJ', CNPJ)

            if select_senha and select_senha[0] == senha:
                user = self.selectWHERE('*', 'empresa', 'CNPJ', CNPJ)
                bairro = self.selectWHERE('nome_bairro', 'bairro', 'cod_bairro', user[5])

                return Empresa(user, bairro[0])

        return False

    def logarInstituicao(self):
        CNPJ = input("CNPJ: ")
        if not self.__validar.CNPJ(CNPJ):
            return False

        senha = input("Senha: ")
        conf_senha = input("Confirme a senha: ")
        if not self.__validar.Senha(senha, conf_senha):
            return False

        if self.__validar.chaveExiste('CNPJ', 'instituicao', CNPJ):
            select_senha = self.selectWHERE('senha', 'instituicao', 'CNPJ', CNPJ)

            if select_senha and select_senha[0] == senha:
                user = self.selectWHERE('*', 'instituicao', 'CNPJ', CNPJ)
                bairro = self.selectWHERE('nome_bairro', 'bairro', 'cod_bairro', user[5])

                return Instituicao(user, bairro[0])

        return False
    

