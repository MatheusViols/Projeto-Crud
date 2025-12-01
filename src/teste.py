from CRUD.Read import Read
from Dados import *


buscar = Read(Chave())

select = buscar.selectVagas(1)
print(select)

vagas = DadosVagas(select)

for vaga in vagas.dados:
    print(f"{vaga} - {vagas.dados[vaga]}")

