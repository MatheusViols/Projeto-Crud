from CRUD.Create import Create
import mysql.connector

class Instituicao:
    def __init__(self, dados):
        self.__dados = dados

        self.__cursos = None
        self.CURSO_ATRIBUTOS = "cod_curso, nome_curso, quant_vagas, desc_curso, cod_area, cod_turno"

    def info(self):
        print(f"""
                CNPJ: {self.__dados.CNPJ}
                Nome: {self.__dados.nome_inst}
                Endereço: {self.__dados.endereco}
                Descrição: {self.__dados.desc_inst}

                Bairro: {self.__dados.nome_bairro} | Codigo {self.__dados.cod_bairro} 

        """)

    def mostrarCursos(self):
        if not self.__cursos:
            print("Nenhum curso cadastrado")
            return 
        for curso in self.__cursos:
            print(f"""
                codigo: {curso[0]}
                nome: {curso[1]}
                vagas: {curso[2]}
                codigo de área: {curso[4]}
                codigo de turno: {curso[5]}

                descrição: {curso[3]}
            """)
                


    def atualizaCursos(self, cursor):
        try:
            cursor.execute(f"SELECT {self.CURSO_ATRIBUTOS} FROM curso WHERE CNPJ = '{self.__dados.CNPJ}'")
            self.__cursos = cursor.fetchall()
            return True
        except mysql.connector.errors.DatabaseError:
            print("Algo deu errado durante a atualização de cursos, atualização não finalizada")
            return False
        

    def cadastrarCurso(self, cnx, cursor):
        cadastro = Create(cnx, cursor)

        if not cadastro.cadCurso(self.__dados.CNPJ, self.__dados.cod_bairro):
            return False

        return (True if self.atualizaCursos(cursor) else False)

