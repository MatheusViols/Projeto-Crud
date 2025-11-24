from CRUD.Create import Create

class Empresa:
    def __init__(self, dados):
        self.__dados = dados

        self.__vagas = None
        self.VAGA_ATRIBUTOS = "cod_vaga, nome_vaga, quant_vagas, desc_vaga, cod_area, cod_turno"

    def info(self):
        print(f"""
                CNPJ: {self.__dados.CNPJ}
                Nome: {self.__dados.nome_emp}
                Endereço: {self.__dados.endereco}
                Descrição: {self.__dados.desc_emp}

                Bairro: {self.__dados.nome_bairro}  |  codigo: {self.__dados.cod_bairro}
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
            cursor.execute(f"SELECT {self.VAGA_ATRIBUTOS} FROM vaga WHERE CNPJ = '{self.__dados.CNPJ}'")
            self.__vagas = cursor.fetchall()
            return True
        except mysql.connector.errors.DatabaseError:
            print("Algo deu errado durante a atualização de vagas, atualização não finalizada")
            return False


    def cadastrarVaga(self, cnx, cursor):
        cadastro = Create(cnx, cursor)

        if not cadastro.cadVaga(self.__dados.CNPJ, self.__dados.cod_bairro):
            return False

        return (True if self.atualizaVagas(cursor) else False)

