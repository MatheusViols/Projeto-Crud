import mysql.connector

class Read:
    def __init__(self, cnx, cursor):
        self.__cnx = cnx
        self.__cursor = cursor

        self.VAGAS_SELECT ="""
                SELECT
                cod_vaga, nome_vaga, quant_vagas, desc_vaga,
                nome_area, nome_turno, nome_emp, nome_bairro
                FROM
                vaga v, empresa e, area a, turno t, bairro b
                WHERE
                v.cod_area = {} AND
                v.CNPJ = e.CNPJ AND
                v.cod_area = a.cod_area AND
                v.cod_turno = t.cod_turno AND
                v.cod_bairro = b.cod_bairro;
                """

        self.APLI_SELECT ="""
                SELECT 
                nome_vaga, status_apli
                FROM
                aplica ap, vaga v
                WHERE
                ap.CPF = {} AND
                ap.cod_vaga = v.cod_vaga
                """


    def selectWhere(self, atributo, tabela, filtro):
        self.__cursor.execute(f"SELECT {atributo} FROM {tabela} WHERE {filtro};")
        return self.__cursor.fetchall()

    def selectVagas(self, cod_area):
        try:
            self.__cursor.execute(self.VAGAS_SELECT.format(cod_area))
            return self.__cursor.fetchall()
        except mysql.connector.errors.DatabaseError:
            print("Algo deu errado durante a execução, não foi possivel selecionar vagas")
            return False


    def selectAplicacoes(self, CPF):
            self.__cursor.execute(self.APLI_SELECT.format(CPF))
            return self.__cursor.fetchall()
            



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
        # Retorna True se o usuario existe, False se não foi encontrado
        usuario = self.usuarioExiste(login)

        # Se usuario existe e informou a senha correta, mostra as informações
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





        

