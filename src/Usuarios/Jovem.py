from CRUD.Create import Create
from CRUD.Read import Read
from CRUD.Update import Update
from CRUD.Delete import Delete

from Dados import *

class Jovem:
    def __init__(self, dados, chave):
        self.__dados = dados
        self.__chave = chave

        self.__aplicacoes = None
        self.__matriculas = None

        self.atualizaAplicacoes()
        self.atualizaMatriculas()

        self.tipo = 'Jovem'


    def info(self):
        print(f"""
                CPF: {self.__dados.CPF}
                Nome: {self.__dados.nome_comp}
                Data de nascimento: {self.__dados.data_nasc}
                Telefone: {self.__dados.telefone}
                Endereço: {self.__dados.endereco}
                Descrição: {self.__dados.desc_user}

                Área: {self.__dados.nome_area} Codigo: {self.__dados.cod_area}
                Bairro: {self.__dados.nome_bairro} Codigo: {self.__dados.cod_bairro}
        """)


    def verVagas(self):
        buscar = Read(self.__chave)
        vagas = buscar.selectVagas(self.__dados.cod_area)
        if not vagas:
            print("Nenhuma vaga encontrada")
            return False

        for vaga in vagas:
            print(f"""
                Codigo: {vaga[0]} | Nome: {vaga[1]}
                Empresa: {vaga[5]}
                Área: {vaga[3]}
                Turno: {vaga[4]}
                Bairro: {vaga[6]}
                Vagas: {vaga[2]}

                Descrição: {vaga[7]}
            """)

    def verAplicacoes(self):
        if not self.__aplicacoes:
            print("Você não tem aplicações para nenhuma vaga")
            return False

        for aplicacao in self.__aplicacoes:
            print(f"""
                Nome: {aplicacao[0]}
                Status {'Em espera' if aplicacao[1] == 0 else 'Aprovada'}

            """)



    def aplicarVaga(self):
        buscar = Read(self.__chave)
        cadastro = Create(self.__chave)
        
        while True:
            try:
                cod_vaga = int(input("Código da vaga: "))
                break
            except ValueError:
                print("Código de vaga só pode ser um numero inteiro")
                continue

        ap_existe = buscar.selectOneWhere('*',
                                          'aplica',
                                          f"CPF = '{self.__dados.CPF}' AND cod_vaga = {cod_vaga}")
        if ap_existe:
            print("Você já aplicou para essa vaga, apenas espere")
            return

        vaga = buscar.selectOneWhere('cod_vaga', 'vaga', f'cod_vaga = {cod_vaga}')

        if not vaga:
            print("Não foi encontrada uma vaga com esse código")
            return False

        if not cadastro.cadAplicacao(self.__dados.CPF, cod_vaga):
            return False

        self.atualizaAplicacoes()

    def removerAplicacao(self):
        input_cod_vaga = int(input("Digite o código da vaga que quer retirar a aplicação: "))

        remover = Delete(Chave())

        if not remover.deleteWhere('aplica', f"CPF = '{self.__dados.CPF}' AND cod_vaga = {input_cod_vaga}"):
            print("Código de vaga não encontrado")
            return False

        self.atualizaAplicacoes()

        return True

        


    def atualizaAplicacoes(self):
        buscar = Read(self.__chave)
        aplicacoes = buscar.selectAplicacoes(self.__dados.CPF)
        self.__aplicacoes = aplicacoes
        if not aplicacoes:
            return False




    def verCursos(self):
        buscar = Read(self.__chave)
        cursos = buscar.selectCursos(self.__dados.cod_area)
        if not cursos:
            print("Nenhum curso encontrado")
            return False

        for curso in cursos:
            print(f"""
                Codigo: {curso[0]} | Nome: {curso[1]}
                Instituição: {curso[6]}
                Área: {curso[4]}
                Turno: {curso[5]}
                Bairro: {curso[7]}
                Vagas: {curso[2]}

                Descrição: {curso[3]}
            """)
        
    def verMatriculas(self):
        if not self.__matriculas:
            print("Você ainda não tem nenhuma matricula")
            return False
        for matricula in self.__matriculas:
            print(f"""
                Nome: {matricula[0]}
                Status {'Em espera' if matricula[1] == 0 else 'Aprovada'}

            """)

        
    def matricularCurso(self):
        cadastrar = Create(self.__chave)
        buscar = Read(self.__chave)

        while True:
            try:
                cod_curso = int(input("Código de curso: "))
                break
            except ValueError:
                print("Código de curso só pode ser um número inteiro")
                continue

        mat_existe = buscar.selectOneWhere('*',
                                           'matricula',
                                           f"CPF = '{self.__dados.CPF}' AND cod_curso = {cod_curso}")

        if mat_existe:
            print("Você já está matriculado nesse curso, apenas aguarde")
            return

        curso = buscar.selectOneWhere('cod_curso', 'curso', f'cod_curso = {cod_curso}')

        if not curso:
            print("Não foi encontrada um curso com esse código")
            return False

        if not cadastrar.cadMatricula(self.__dados.CPF, cod_curso):
            return False

        self.atualizaMatriculas()

    def removerMatricula(self):
        input_cod_mat = int(input("Digite o código do curso que quer retirar a matricula: "))

        remover = Delete(Chave())

        if not remover.deleteWhere('matricula', f"CPF = '{self.__dados.CPF}' AND cod_curso = {input_cod_mat}"):
            print("Código de curso não encontrado")
            return False


        self.atualizaMatriculas()

        return True



    def atualizaMatriculas(self):
        buscar = Read(self.__chave)
        matriculas = buscar.selectMatriculas(self.__dados.CPF)

        self.__matriculas = matriculas
        if not matriculas:
            print("Nenhuma matricula realizada")
            return False



    def atualizarDados(self):
        while True:
            dicio_dados = {
                    '1':('nome_comp',  lambda: InputValido('Digite o novo nome', 'nome')),
                    '2':('data_nasc',  lambda: InputDataValida()),
                    '3':('telefone',   lambda: InputValido('Digite o novo telefone', 'telefone')),
                    '4':('endereco',   lambda: InputValido('Digite o novo endereço', 'endereco')),
                    '5':('desc_user',  lambda: InputValido('Digite o novo descrição', 'descricao')),
                    '6':('cod_bairro', lambda: InputValido('Digite o novo codigo de bairro', 'bairro')),
                    '7':('cod_area',   lambda: InputValido('Digite o novo codigo de área', 'area'))
                                }
            for dado in dicio_dados:
                print(f"{dado} - {dicio_dados[dado]}")

            codigo_dado = input("Digite o código para o tipo de dado que quer atualizar: ")
            if codigo_dado == 'sair': return 
            if not codigo_dado or codigo_dado not in dicio_dados: 
                print("Código não está na lista")
                continue

            ATRIBUTO = dicio_dados[codigo_dado][0]
            INPUT_VALOR = dicio_dados[codigo_dado][1]
            VALOR = INPUT_VALOR()



            atualizar = Update(self.__chave)
            atualizar.updateWhere('usuario',
                                  ATRIBUTO,
                                  f"'{VALOR.dado}'",
                                  f"CPF = '{self.__dados.CPF}' AND senha = '{self.__dados.senha}'")

            buscar = Read(self.__chave)
            select = buscar.selectOneWhere('u.*, nome_area, nome_bairro',
                                                 'usuario u, area ar, bairro b',
                                                 f"CPF = '{self.__dados.CPF}' AND senha = '{self.__dados.senha}'")
            self.__dados = DadosJovem(select)


    def deletarConta(self):
        print("Você tem total certeza de que deseja deletar sua conta?")
        confirmacao = input("-> ").lower()

        if confirmacao == 'sim':
            input_senha = input("Digite a sua senha: ")
            conf_input_senha = input("Confirme sua senha: ")

            if (input_senha and conf_input_senha) and (input_senha == conf_input_senha) and (input_senha == self.__dados.senha):
                deletar = Delete(Chave())

                deletar.deleteWhere('usuario', f"CPF = '{self.__dados.CPF}'")
                return True

            else: 
                print("Senha incorreta")
                return False

        else: 
            return False


                




            









