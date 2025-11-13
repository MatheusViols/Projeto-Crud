from CRUD.Usuarios.Usuario import Usuario

class Read:
    def __init__(self, lista):
        self.__lista = lista

    def usuarioExiste(self, login):
        for usuario in self.__lista:
            if login == usuario.login:
                return usuario
        return False

    def validaUsuario(self, usuario, senha):
        return senha == usuario.senha

    def mostraUsuario(self, login, senha):
        usuario = self.usuarioExiste(login)
        if usuario and self.validaUsuario(usuario, senha):
            print(f"""
                {usuario.login}
                {usuario.nome} {usuario.sobrenome}
                {usuario.endereco}
                """)




        

