import mysql.connector

cnx = mysql.connector.connect(user='crud-user', password='crud-user', host='localhost', database='crud')
cursor = cnx.cursor()

usuario = "usuario(CPF, senha, nome_comp, data_nasc, telefone, endereco, desc_user, cod_area, cod_bairro)"
values = "'16178162345', 'boberto', 'Rodrigo Paiva', '2003-08-08', '81989226723', 'Rua do Padre', 'Apenas', 1, 14"
cursor.execute(f"INSERT INTO {usuario} VALUES({values});" )
