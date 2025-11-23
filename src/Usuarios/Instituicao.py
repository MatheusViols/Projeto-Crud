from CRUD.Create import Create
import mysql.connector

class Instituicao:
    def __init__(self, atts, bairro):
        self.__CNPJ = atts[0]
        self.__senha = atts[1]
        self.__nome_inst = atts[2]
        self.__endereco = atts[3]
        self.__desc = atts[4]
        self.__cod_bairro = atts[5]


        self.__nome_bairro = bairro 

        self.__cursos = None
        self.CURSO_ATRIBUTOS = "cod_curso, nome_curso, quant_vagas, desc_curso, cod_area, cod_turno"

    def info(self):
        print(f"""
                CNPJ: {self.__CNPJ}
                Nome: {self.__nome_inst}
                Endereço: {self.__endereco}
                Descrição: {self.__desc}

                Bairro: {self.__nome_bairro} | Codigo {self.__cod_bairro} 

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
            cursor.execute(f"SELECT {self.CURSO_ATRIBUTOS} FROM curso WHERE CNPJ = '{self.__CNPJ}'")
            self.__cursos = cursor.fetchall()
            return True
        except mysql.connector.errors.DatabaseError:
            print("Algo deu errado durante a atualização de cursos, atualização não finalizada")
            return False
        

    def cadastrarCurso(self, cnx, cursor):
        cadastro = Create(cnx, cursor)

        if not cadastro.cadCurso(self.__CNPJ, self.__cod_bairro):
            return False

        return (True if self.atualizaCursos(cursor) else False)

