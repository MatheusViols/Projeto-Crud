from CRUD.Usuarios.Usuario import Usuario

class Create:
    def __init__(self, lista):
        self.__lista = lista

    def validaLogin(self, login):
        for usuario in self.__lista:
            if login == usuario.login:
                print("Erro: Login já está em uso") 
                return False

        return True

    def validaSenha(self, senha):
        if not senha or senha.isspace():
            print("Erro: Senha não pode ser vazia")
            return False


        confSenha = input("Confirme a senha: ")
        if confSenha != senha:
            print("Erro: Senhas diferentes")
            return False

        if " " in senha:
            print("Erro: Senha não pode ter espaços em branco")
            return False

        return True

    def validaNome(self, nome):
        if not nome or nome.isspace():
            print("Erro: Nome não pode ser vazio")
            return False

        if " " in nome:
            print("Erro: Sem espaços em branco, apenas o primeiro nome")
            return False

        return True

    def validaSobrenome(self, sobrenome):
        if not sobrenome or sobrenome.isspace():
            print("Erro: Sobrenome não pode ser vazio")
            return False

        if " " in sobrenome:
            print("Erro: Sem espaços em branco, apenas o sobrenome")
            return False

        return True


    def validaEndereco(self, endereco):
        if not endereco or endereco.isspace():
            print("Erro: Endereço não pode ser vazio")
            return False

        return True

    def criarUsuario(self):
        login = input("login: ")
        if not self.validaLogin(login): 
            return False

        senha = input("senha: ")
        if not self.validaSenha(senha): 
            return False

        nome = input("nome: ")
        if not self.validaNome(nome):
            return False

        sobrenome = input("sobrenome: ")
        if not self.validaSobrenome(sobrenome):
            return False

        endereco = input("Endereço: ")
        if not self.validaEndereco(endereco):
            return False

        return Usuario(login, senha, nome, sobrenome, endereco)


