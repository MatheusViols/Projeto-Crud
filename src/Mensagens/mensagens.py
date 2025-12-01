MSG_INICIAL = """
     ---------->> Conecta Igarassu <<----------
            Bem vindo ao programa Conecta Igarassu

            Nosso objetivo: Conectar jovens à vagas
            de emprego ou de cursos profissionaliza
            ntes

            Antes de tudo, você já possui login?
            (Responda com Sim ou Não)
            Se deseja sair do programa, digite Sair



"""
MSG_TIPO_CAD = """
            Que tipo de conta deseja cadastrar?
            1 - Jovem
            2 - Empresa
            3 - Instituição de Ensino

"""



MSG_CAD_EMP = """
            Para sua conta de empresa vamos precisar:
            - CNPJ (apenas números)
            - Nome da empresa
            - Bairro
            - Endereço
            - Descrição da empresa de até 100 caracteres

"""

MSG_CAD_INST = """
            Para sua conta de instituição de ensino vamos precisar:
            - CNPJ (apenas números)
            - Nome da instituição
            - Bairro
            - Endereço
            - Descrição da instituição de até 100 caracteres

"""

MSG_CAD_JOVEM = """
            Para sua conta de jovem vamos precisar:
            - Seu CPF (apenas números)
            - Nome completo
            - Data de nascimento
            - Número de telefone (apenas números incluindo DDD)
            - Bairro
            - Endereço
            - Área de interesse para trabalho ou estudo
            - Descrição pessoal de até 100 caracteres

"""
MSG_COD_BAIRRO= """

+------+---------------------------+------+---------------------------+
| Cod. | Bairro                    | Cod. | Bairro                    |
+------+---------------------------+------+---------------------------+
| 1    | Agamenon Magalhães        | 2    | Alto do Céu               |
| 3    | Ana de Albuquerque        | 4    | Arassoiaba                |
| 5    | Área Rural de Igarassu    | 6    | Bela Vista                |
| 7    | Bonfim                    | 8    | Campina de Feira          |
| 9    | Centro                    | 10   | Cruz de Reboucas          |
| 11   | Distrito de Três Ladeiras | 12   | Distrito Industrial       |
| 13   | Distrito Nova Cruz        | 14   | Encanto Igarassu          |
| 15   | Inhamã                    | 16   | Jabacó                    |
| 17   | Jardim Boa Sorte          | 18   | Monjope                   |
| 19   | Pancó                     | 20   | Vila Rural                |
| 21   | Posto de Monta            | 22   | Rubina                    |
| 23   | Santa Luzia               | 24   | Santa Rita                |
| 25   | Santo Antônio             | 26   | Saramandaia               |
| 27   | Sítio dos Marcos          | 28   | Tabatinga                 |
| 29   | Triunfo                   | 30   | Umbura                    |
| 31   | Cuieiras                  |      |                           |
+------+---------------------------+------+---------------------------+

"""

MSG_COD_AREA = """
+------+---------------------------+
| Cod. | Area                      |
+------+---------------------------+
| 1    | TI                        |
| 2    | Saúde                     |
| 3    | Design                    |
| 4    | Marketing                 |
| 5    | Industrial                |
| 6    | Administração             |
| 7    | Setor Público             |
+------+---------------------------+

"""

MSG_COD_TURNO = """
+------+---------------------------+
| Cod. | Turno                     |
+------+---------------------------+
| 1    | Manhã                     |
| 2    | Tarde                     |
| 3    | Noite                     |
+------+---------------------------+

"""
MSG_DESC = """
            Agora nos dê uma breve descrição de no maximo
            100 caracteres, tente não passar disso, a partir do
            caractere 100 tudo será ignorado e sua descrição ficará
            incompleta
            Caso não queira fazer isso agora, o campo é opicional
            e pode ser deixado em branco para preencher futuramente
"""

MSG_SENHA = """
            Por fim, escolha uma senha da qual consiga lembrar e que
            seja segura. A senha deve conter de 5 a 11 caracteres po
            dendo serem letras, numeros e caracteres especiais.
            NÃO SÃO PERMITIDOS ESPAÇOS EM BRANCO
            Logo em seguida será pedido que confirme a senha digitada

"""

MSG_TIPO_LOGIN = """
            Para logar, primeiro selecione o tipo de conta em que deseja
            logar entre as opções:

            1 - Jovem
            2 - Empresa
            3 - Instituição
"""

MSG_LOGIN_JOVEM = """
            Para logar como Jovem você precisará fornecer:
            - Seu CPF (apenas números)
            - A senha cadastrada junto ao seu perfil

"""

MSG_LOGIN_EMP_INST = """
            Para logar você precisará fornecer:
            - Seu CNPJ (apenas números)
            - A senha cadastrada junto ao seu perfil

"""

COMANDOS_JOVEM = { 
            '1':'Ver minhas informações',
            '2':'Ver vagas da minha área',
            '3':'Ver minhas aplicações',
            '4':'Aplicar para vaga',
            '5':'Remover aplicação',
            '6':'Ver Cursos da minha área',
            '7':'Ver minhas matriculas',
            '8':'Matricular em um curso',
            '9':'Remover matricula',
            '10':'Atualizar meus dados',
            '11':'Deletar minha conta'
                  }


COMANDOS_EMP = { 
            '1':'Ver minhas informações',
            '2':'Ver minhas vagas',
            '3':'Cadastrar nova vaga',
            '4':'Remover vaga',
            '5':'Atualizar meus dados',
            '6':'Deletar minha conta'
            }

COMANDOS_INST = {
            '1':'Ver minhas informações',
            '2':'Ver meus cursos',
            '3':'Cadastrar novo curso',
            '4':'Remover curso',
            '5':'Atualizar meus dados',
            '6':'Deletar minha conta'
            }
