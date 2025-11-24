import mysql.connector

class Read:
    def __init__(self, chave):
        self.__cnx = chave.cnx
        self.__cursor = chave.cursor

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
                ap.CPF = '{}' AND
                ap.cod_vaga = v.cod_vaga
                """

        self.CURSOS_SELECT ="""
                SELECT
                cod_curso, nome_curso, quant_vagas, desc_curso,
                nome_area, nome_turno, nome_inst, nome_bairro
                FROM
                curso c, instituicao i, area a, turno t, bairro b
                WHERE
                c.cod_area = {} AND
                c.CNPJ = i.CNPJ AND
                c.cod_area = a.cod_area AND
                c.cod_turno = t.cod_turno AND
                c.cod_bairro = b.cod_bairro;
                """

        self.MAT_SELECT ="""
                SELECT
                nome_curso, status_mat
                FROM
                matricula mat, curso c
                WHERE
                mat.CPF = {} AND
                mat.cod_curso = c.cod_curso
                """




    def selectOneWhere(self, atributo, tabela, filtro):
        try:
            self.__cursor.execute(f"SELECT {atributo} FROM {tabela} WHERE {filtro};")
            return self.__cursor.fetchone()
        except mysql.connector.errors.DatabaseError:
            print("Algo deu errado durante a execução, não foi possivel selecionar um elemento")
            return False

    def selectAllWhere(self, atributo, tabela, filtro):
        try:
            self.__cursor.execute(f"SELECT {atributo} FROM {tabela} WHERE {filtro};")
            return self.__cursor.fetchall()
        except mysql.connector.errors.DatabaseError:
            print("Algo deu errado durante a execução, não foi possivel selecionar todos os elementos")
            return False

    def selectVagas(self, cod_area):
        try:
            self.__cursor.execute(self.VAGAS_SELECT.format(cod_area))
            return self.__cursor.fetchall()
        except mysql.connector.errors.DatabaseError:
            print("Algo deu errado durante a execução, não foi possivel selecionar vagas")
            return False


    def selectAplicacoes(self, CPF):
        try:
            self.__cursor.execute(self.APLI_SELECT.format(CPF))
            return self.__cursor.fetchall()
        except mysql.connect.errors.DatabaseError:
            print("Algo deu errado durante a execução, não foi possivel selecionar aplicações")
            return False

    def selectCursos(self, cod_area):
        try:
            self.__cursor.execute(self.CURSOS_SELECT.format(cod_area))
            return self.__cursor.fetchall()
        except mysql.connector.errors.DatabaseError:
            print("Algo deu errado durante a execução, não foi possivel selecionar cursos")
            return False
            
    def selectMatriculas(self, CPF):
        try:
            self.__cursor.execute(self.MAT_SELECT.format(CPF))
            return self.__cursor.fetchall()
        except mysql.connector.errors.DatabaseError:
            print("Algo deu errado durante a execução, não foi possivel selecionar matriculas")
            return False

