from CRUD.Create import Create 
from CRUD.Read import Read

from CRUD.Usuarios.Usuario import Usuario




lista = []

lista.append( Usuario('01818816', 'sinistro', 'matheus', 'vinicius', 'avenida liberdade') )
lista.append( Usuario('01814030', 'rapaz', 'bob', 'cenora', 'rua querencia do norte') )

while True:
    uso = input("[ CRUD ] $ ")

    if uso == 'create':
        criar = Create(lista)
        criar.criarUsuario()
    elif uso == 'show':
        login = input("login: ")
        senha = input("senha: ")

        ler = Read(lista)
        ler.mostraUsuario(login, senha)
    elif uso == 'sair':
        break








