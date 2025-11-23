from CRUD.Create import Create

class Empresa:
    def __init__(self, atts, bairro):
        self.__CNPJ = atts[0]
        self.__senha = atts[1]
        self.__nome_emp = atts[2]
        self.__endereco = atts[3]
        self.__desc = atts[4]
        self.__cod_bairro = atts[5]

        self.__bairro = bairro 

        self.__vagas = None
        self.VAGA_ATRIBUTOS = "cod_vaga, nome_vaga, quant_vagas, desc_vaga, cod_area, cod_turno"

    def info(self):
        print(f"""
                CNPJ: {self.__CNPJ}
                Nome: {self.__nome_emp}
                Endereço: {self.__endereco}
                Descrição: {self.__desc}

                Bairro: {self.__bairro}  |  codigo: {self.__cod_bairro}
        """)

    def mostrarVagas(self):
        if not self.__vagas:
            print("Nenhuma vaga cadastrada")
            return
        for vaga in self.__vagas:
            print(f"""
                codigo: {vaga[0]}
                nome: {vaga[1]}
                vagas: {vaga[2]}
                codigo de área: {vaga[4]}
                codigo de turno: {vaga[5]}

                descrição: {vaga[3]}
            """)



    def atualizaVagas(self, cursor):
        try:
            cursor.execute(f"SELECT {self.VAGA_ATRIBUTOS} FROM vaga WHERE CNPJ = '{self.__CNPJ}'")
            self.__vagas = cursor.fetchall()
            return True
        except mysql.connector.errors.DatabaseError:
            print("Algo deu errado durante a atualização de vagas, atualização não finalizada")
            return False


    def cadastrarVaga(self, cnx, cursor):
        cadastro = Create(cnx, cursor)

        if not cadastro.cadVaga(self.__CNPJ, self.__cod_bairro):
            return False

        return (True if self.atualizaVagas(cursor) else False)

