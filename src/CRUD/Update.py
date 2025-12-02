import mysql.connector
from CRUD.Read import Read
from CRUD.Valida import Valida

class Update:
    def __init__(self, chave):
        self.__chave = chave
        self.__cnx = chave.cnx
        self.__cursor = chave.cursor

        self.__buscar = Read(chave)
        self.__validar = Valida(chave)


    def updateWhere(self, tabela, atributo, valor, filtro):
        try:
            self.__cursor.execute(f"UPDATE {tabela} SET {atributo} = {valor} WHERE {filtro}")
            self.__cnx.commit()
        except mysql.connector.errors.DatabaseError:
            print("Não foi possivel atualizar")
            return False


