def cadastrar_aluno(alunos):
    nome = input("Nome: ").lower()
    idade = int(input("Idade: "))
    nota = float(input("Nota: "))
    ficha = {"nome": nome,
             "idade": idade,
             "nota": nota}
    alunos.append(ficha)


def menu():
    print("""
    ===============
    Sistema Escolar
    ================

    1 - Cadastrar aluno
    2 - Listar alunos
    3 - Buscar aluno
    4 - Alterar nota
    5 - Remover aluno
    6 - Sair
    """)


def listar_alunos(alunos):
    for i in alunos:
        print(f"""
        ---------------------
        Nome: {i['nome']}
        Idade: {i['idade']}
        Nota: {i['nota']}
        ---------------------""")


def buscar_aluno(alunos):
    nomeProcurado = input("Nome para busca: ").strip().lower()
    encontrado = False
    for i in alunos:
        if nomeProcurado == i['nome']:
            print("Aluno encontrado!")
            print("")
            print(f"""
            Nome: {i['nome']}
            Idade: {i['idade']}
            Nota: {i['nota']}
            """)
            encontrado = True
            break
    if not encontrado:
        print("Aluno não encontrado.")


def alterar_nota(alunos):
    nomeAlterar = input("Nome para alteração: ").strip().lower()
    encontrado = False
    for i in alunos:
        if nomeAlterar == i['nome']:
            novaNota = float(input("Nova nota: "))
            i['nota'] = novaNota
            encontrado = True
            print("Nota alterada com sucesso!")
            break
    if not encontrado:
        print("Aluno não encontrado")


def remover_aluno(alunos):
    nomeRemover = input("Nome para remoção: ").strip().lower()
    encontrado = False
    for i in alunos:
        if nomeRemover == i['nome']:
            alunos.remove(i)
            encontrado = True
            print("Aluno removido com sucesso!")
            break
    if not encontrado:
        print("Aluno não encontrado!")


