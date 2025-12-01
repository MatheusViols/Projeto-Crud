import mysql.connector

class Delete:
    def __init__(self, chave):
        self.__chave = chave
        self.__cnx = chave.cnx
        self.__cursor = chave.cursor


    def deleteWhere(self, tabela, filtro):
        try:
            self.__cursor.execute(f"DELETE FROM {tabela} WHERE {filtro}")
            self.__cnx.commit()
            return True
        except mysql.connector.errors.DatabaseError:
            print("Algo deu errado, não foi possivel remover os dados")
            return False

    def deleteWhereERRO(self, tabela, filtro):
        self.__cursor.execute(f"DELETE FROM {tabela} WHERE {filtro}")
        self.__cnx.commit()
        return True

    def deleteCascade(self, tabelas_filhas, tabela_pai, filtro):
        for tabela in tabelas_filhas:
            self.deleteWhere(tabela, filtro)

        self.deleteWhere(tabela_pai, filtro)




    

