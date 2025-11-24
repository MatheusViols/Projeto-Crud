from Mensagens import mensagens
from CRUD.Valida import Valida

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
        CPF = input("CPF: ")
        if not self.__validar.CPF(CPF):
            return False
        if self.__validar.chaveExiste('CPF', 'usuario', CPF):
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
        area = input("Código da área: ")
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
        desc_inst = self.__validar.Desc(desc_inst) 

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
        desc_curso = self.__validar.Desc(desc_curso)

        
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
        desc_vaga = self.__validar.Desc(desc_vaga)

        
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
        return (True if self.insert(self.MAT_ATRIBUTOS, valores) else False)









        
        

