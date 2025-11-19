from Mensagens import mensagens
from CRUD.Valida import Valida

import mysql.connector
 

class Create:
    def __init__(self, cnx, cursor):
        self.__cnx = cnx
        self.__cursor = cursor
        self.__validar = Valida(cnx, cursor)

        self.JOVEM_ATRIBUTOS = "usuario(CPF, senha, nome_comp, data_nasc, telefone, endereco, desc_user, cod_area, cod_bairro)"
        self.EMP_ATRIBUTOS = "empresa(CNPJ, senha, nome_emp, endereco, desc_emp, cod_bairro)"
        self.INST_ATRIBUTOS = "instituicao(CNPJ, senha, nome_inst, endereco, desc_inst, cod_bairro)"




    def insert(self, tabela, valores):
        try:
            self.__cursor.execute(f"INSERT INTO {tabela} VALUES({valores});")
            self.__cnx.commit()
            return True
        except mysql.connector.errors.DatabaseError:
            print("Erro: Algo deu errado durante a inserção de dados, cadastro não finalizado")
            return False


    def cadJovem(self):
        CPF = input("CPF: ")
        if not self.__validar.CPF(CPF):
            return False
        if self.__validar.CPFExiste(CPF):
            print("ERRO: CPF Já cadastrado")
            return False

        nome_comp = input("Nome completo: ")
        if not self.__validar.Nome(nome_comp):
            return False

        dia = input("Dia de nascimento: ")
        mes = input("Mês de nascimento: ")
        ano = input("Ano de nascimento: ")
        if not self.__validar.Data(dia, mes, ano):
            return False

        telefone = input("Telefone: ")
        if not self.__validar.Telefone(telefone):
            return False

        print(mensagens.MSG_COD_BAIRRO)
        bairro = input("Bairro: ") 
        if not self.__validar.Bairro(bairro):
            return False

        endereco = input("Endereço: ")
        if not self.__validar.Endereco(endereco):
            return False

        print(mensagens.MSG_COD_AREA)
        area = input("Área: ")
        if not self.__validar.Area(area):
            return False

        print(mensagens.MSG_DESC)
        desc_user = input("Descrição: ")
        desc_user = self.__validar.Desc(desc_user) 

        print(mensagens.MSG_SENHA)
        senha = input("Senha: ")
        conf_senha = input("Confirme a senha: ")
        if not self.__validar.Senha(senha, conf_senha):
            return False

        

        valores = f"'{CPF}', '{senha}', '{nome_comp}', '{ano}-{mes}-{dia}', '{telefone}', '{endereco}', '{desc_user}', {area}, {bairro}"
        return (True if self.insert(self.JOVEM_ATRIBUTOS, valores) else False)

        
    def cadEmpresa(self):
        CNPJ = input("CNPJ: ")
        if not self.__validar.CNPJ(CNPJ):
            return False
        if self.__validar.CNPJEmpExiste(CNPJ):
            print("Erro: CNPJ já cadastrado")
            return False

        nome_emp = input("Nome completo: ")
        if not self.__validar.Nome(nome_emp):
            return False

        print(mensagens.MSG_COD_BAIRRO)
        bairro = input("Bairro: ") 
        if not self.__validar.Bairro(bairro):
            return False

        endereco = input("Endereço: ")
        if not self.__validar.Endereco(endereco):
            return False

        print(mensagens.MSG_DESC)
        desc_emp = input("Descrição: ")
        desc_emp = self.__validar.Desc(desc_emp) 

        print(mensagens.MSG_SENHA)
        senha = input("Senha: ")
        conf_senha = input("Confirme a senha: ")
        if not self.__validar.Senha(senha, conf_senha):
            return False


        valores = f"'{CNPJ}', '{senha}', '{nome_emp}', '{endereco}', '{desc_emp}', {bairro}"
        return (True if self.insert(self.EMP_ATRIBUTOS, valores) else False)
         

            

    def cadInstituicao(self):
        CNPJ = input("CNPJ: ")
        if not self.__validar.CNPJ(CNPJ):
            return False
        if self.__validar.CNPJInstExiste(CNPJ):
            print("Erro: CNPJ já cadastrado")
            return False

        nome_inst = input("Nome Instituição: ")
        if not self.__validar.Nome(nome_inst):
            return False

        print(mensagens.MSG_COD_BAIRRO)
        bairro = input("Bairro: ") 
        if not self.__validar.Bairro(bairro):
            return False

        endereco = input("Endereço: ")
        if not self.__validar.Endereco(endereco):
            return False

        print(mensagens.MSG_DESC)
        desc_inst = input("Descrição: ")
        desc_inst = self.__validar.Desc(desc_inst) 

        print(mensagens.MSG_SENHA)
        senha = input("Senha: ")
        conf_senha = input("Confirme a senha: ")
        if not self.__validar.Senha(senha, conf_senha):
            return False


        valores = f"'{CNPJ}', '{senha}', '{nome_inst}', '{endereco}', '{desc_inst}', {bairro}"
        return (True if self.insert(self.INST_ATRIBUTOS, valores) else False)

