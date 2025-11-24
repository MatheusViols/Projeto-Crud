from CRUD.Valida import Valida
from CRUD.Read import Read

from Usuarios.Jovem import Jovem
from Usuarios.Empresa import Empresa
from Usuarios.Instituicao import Instituicao

from Dados import *

class Login:
    def __init__(self, chave):
        self.__chave = chave
        self.__cnx = chave.cnx
        self.__cursor = chave.cursor
        self.__validar = Valida(chave)
        self.__buscar = Read(chave)



    def logarJovem(self):
        CPF = input("CPF: ")
        if not self.__validar.CPF(CPF):
            return False

        input_senha = input("Senha: ")
        conf_senha = input("Confirme a senha: ")
        if not self.__validar.Senha(input_senha, conf_senha):
            return False

        if not self.__validar.chaveExiste('CPF', 'usuario', CPF):
            print("Erro: Esse CPF não está cadastrado")
            return False

        atributos = 'u.*, nome_area, nome_bairro'
        tabelas = 'usuario u, area a, bairro b'
        filtro = f"u.CPF = '{CPF}' AND u.cod_area = a.cod_area AND u.cod_bairro = b.cod_bairro"

        try:
            select = self.__buscar.selectOneWhere(atributos, tabelas, filtro)
        except mysql.connector.errors.DatabaseError:
            print("Algo deu errado, não foi possivel fazer o login")
            return False


        dados = DadosJovem(select)

        return Jovem(dados, self.__chave) if dados.senha == input_senha else False




    def logarEmpresa(self):
        CNPJ = input("CNPJ: ")
        if not self.__validar.CNPJ(CNPJ):
            return False

        input_senha = input("Senha: ")
        conf_senha = input("Confirme a senha: ")
        if not self.__validar.Senha(input_senha, conf_senha):
            return False

        if not self.__validar.chaveExiste('CNPJ', 'empresa', CNPJ):
            print("Erro: CNPJ não cadastrado")
            return False

        atributos = 'e.*, nome_bairro'
        tabelas = 'empresa e, bairro b'
        filtro = f"e.CNPJ = '{CNPJ}' AND e.cod_bairro = b.cod_bairro"

        try:
            select = self.__buscar.selectOneWhere(atributos, tabelas, filtro)
        except mysql.connector.errors.DatabaseError:
            print("")
            return False

        dados = DadosEmpresa(select)

        return Empresa(dados) if dados.senha == input_senha else False

    def logarInstituicao(self):
        CNPJ = input("CNPJ: ")
        if not self.__validar.CNPJ(CNPJ):
            return False

        input_senha = input("Senha: ")
        conf_senha = input("Confirme a senha: ")
        if not self.__validar.Senha(input_senha, conf_senha):
            return False

        if not self.__validar.chaveExiste('CNPJ', 'instituicao', CNPJ):
            print("Erro: CNPJ não cadastrado")
            return False

        atributos = 'i.*, nome_bairro'
        tabelas = 'instituicao i, bairro b'
        filtro = f"i.CNPJ = '{CNPJ}' AND i.cod_bairro = b.cod_bairro"

        try:
            select = self.__buscar.selectOneWhere(atributos, tabelas, filtro)
        except mysql.connect.errors.DatabaseError:
            print("Erro: Algo deu errado, não foi possivel logar")
            return False

        dados = DadosIntituicao(select)

        return Instituicao(dados) if dados.senha == input_senha else False
    

