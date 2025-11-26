from Mensagens import mensagens
from CRUD.Valida import Valida
from Dados import *

import mysql.connector
 

class Create:
    def __init__(self, chave):
        self.__cnx = chave.cnx
        self.__cursor = chave.cursor
        self.__validar = Valida(chave)

        self.JOVEM_ATRIBUTOS = "usuario(CPF, senha, nome_comp, data_nasc, telefone, endereco, desc_user, cod_area, cod_bairro)"
        self.EMP_ATRIBUTOS = "empresa(CNPJ, senha, nome_emp, endereco, desc_emp, cod_bairro)"
        self.INST_ATRIBUTOS = "instituicao(CNPJ, senha, nome_inst, endereco, desc_inst, cod_bairro)"

        self.CURSO_ATRIBUTOS = "curso(nome_curso, quant_vagas, desc_curso, cod_area, cod_turno, CNPJ, cod_bairro)"
        self.VAGA_ATRIBUTOS = "vaga(nome_vaga, quant_vagas, desc_vaga, cod_area, cod_turno, CNPJ, cod_bairro)"


        self.APLI_ATRIBUTOS = "aplica(CPF, cod_vaga)"
        self.MAT_ATRIBUTOS = "matricula(CPF, cod_curso)"




    def insert(self, tabela, valores):
        try:
            self.__cursor.execute(f"INSERT INTO {tabela} VALUES({valores});")
            self.__cnx.commit()
            return True
        except mysql.connector.errors.DatabaseError:
            print("Erro: Algo deu errado durante a inserção de dados, cadastro não finalizado")
            return False

    def insertERRO(self, tabela, valores):
            self.__cursor.execute(f"INSERT INTO {tabela} VALUES({valores});")
            self.__cnx.commit()
            return True


    def cadJovem(self):
        input_CPF = InputValido('Digite seu CPF','CPF')
        if not input_CPF.dado: return False
        if self.__validar.chaveExiste('CPF', 'usuario', input_CPF):
            print("ERRO: CPF Já cadastrado")
            return False

        input_nome = InputValido('Digite seu nome', 'nome')
        if not input_nome.dado: return False

        input_data = InputDataValida()
        if not input_data.dado: return False

        input_telefone = InputValido('Digite seu telefone', 'telefone') 
        if not input_telefone.dado: return False

        print(mensagens.MSG_COD_BAIRRO)
        input_bairro = InputValido('Digite o código do seu bairro', 'bairro') 
        if not input_bairro.dado: return False

        input_endereco = InputValido('Digite seu enderço', 'endereco')
        if not input_endereco.dado: return False

        print(mensagens.MSG_COD_AREA)
        input_area = InputValido('Digite o código da sua área', 'area') 
        if not input_area.dado: return False

        print(mensagens.MSG_DESC)
        input_desc = InputValido('Digite sua descrição', 'descricao')
        if not input_desc.dado: return False

        print(mensagens.MSG_SENHA)
        input_senha = InputValido('Digite sua senha: ', 'senha')
        if not input_senha.dado: return False

        

        valores = f"'{input_CPF.dado}', '{input_senha.dado}', '{input_nome.dado}', '{input_data.dado}', '{input_telefone.dado}', '{input_endereco.dado}', '{input_desc.dado}', {input_area.dado}, {input_bairro.dado}"
        return (True if self.insertERRO(self.JOVEM_ATRIBUTOS, valores) else False)

        
    def cadEmpresa(self):
        CNPJ = input("CNPJ: ")
        if not self.__validar.CNPJ(CNPJ):
            return False
        if self.__validar.chaveExiste('CNPJ', 'empresa', CNPJ):
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
        if not self.__validar.Desc(desc_emp):
            return False


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
        if self.__validar.chaveExiste('CNPJ', 'instituicao', CNPJ):
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
        if not self.__validar.Desc(desc_inst):
            return False

        print(mensagens.MSG_SENHA)
        senha = input("Senha: ")
        conf_senha = input("Confirme a senha: ")
        if not self.__validar.Senha(senha, conf_senha):
            return False


        valores = f"'{CNPJ}', '{senha}', '{nome_inst}', '{endereco}', '{desc_inst}', {bairro}"
        return (True if self.insert(self.INST_ATRIBUTOS, valores) else False)

    def cadCurso(self, CNPJ, cod_bairro):
        nome_curso = input("Nome do curso: ")
        if not self.__validar.nomeCurso(nome_curso):
            return False

        quant_vagas = 0
        while True:
            try:
                quant_vagas = int(input("Quantidade de vagas: "))
                break
            except ValueError:
                print("Por favor, digite apenas números")
                continue
            except OverflowError:
                print("Por favor, digite uma quantidade realista")
                continue

            if quant_vagas > 500:
                print("Por favor, digite uma quantidade realista")
                continue

        print(mensagens.MSG_DESC)
        desc_curso = input("Descrição: ")
        if not self.__validar.Desc(desc_curso):
            return False

        
        print(mensagens.MSG_COD_AREA)
        cod_area = input("Código da área: ")
        if not self.__validar.Area(cod_area):
            return False

        print(mensagens.MSG_COD_TURNO)
        cod_turno = input("Código de turno: ")
        if not self.__validar.Turno(cod_turno):
            return False

        valores = f"'{nome_curso}', {quant_vagas}, '{desc_curso}', {cod_area}, {cod_turno}, '{CNPJ}', {cod_bairro}"
        return (True if self.insert(self.CURSO_ATRIBUTOS, valores) else False)


    def cadVaga(self, CNPJ, cod_bairro):
        nome_vaga = input("Nome da vaga: ")
        if not self.__validar.nomeVaga(nome_vaga):
            return False

        quant_vagas = 0
        while True:
            try:
                quant_vagas = int(input("Quantidade de vagas: "))
                break
            except ValueError:
                print("Por favor, digite apenas números")
                continue
            except OverflowError:
                print("Por favor, digite uma quantidade realista")
                continue

            if quant_vagas > 500:
                print("Por favor, digite uma quantidade realista")
                continue

        print(mensagens.MSG_DESC)
        desc_vaga = input("Descrição: ")
        if not self.__validar.Desc(desc_vaga):
            return False

        
        print(mensagens.MSG_COD_AREA)
        cod_area = input("Código da área: ")
        if not self.__validar.Area(cod_area):
            return False

        print(mensagens.MSG_COD_TURNO)
        cod_turno = input("Código de turno: ")
        if not self.__validar.Turno(cod_turno):
            return False

        valores = f"'{nome_vaga}', {quant_vagas}, '{desc_vaga}', {cod_area}, {cod_turno}, '{CNPJ}', {cod_bairro}"
        return (True if self.insert(self.VAGA_ATRIBUTOS, valores) else False)

    def cadAplicacao(self, CPF, cod_vaga):
        valores = f"'{CPF}', {cod_vaga}"
        return (True if self.insert(self.APLI_ATRIBUTOS, valores) else False)

    def cadMatricula(self, CPF, cod_curso):
        valores = f"'{CPF}', {cod_curso}"
        return (True if self.insertERRO(self.MAT_ATRIBUTOS, valores) else False)









        
        

