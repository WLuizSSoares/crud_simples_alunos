def cadastrar_aluno(alunos):


        while True:
            try:
                nome = input("Nome: ").strip().lower()
                idade = int(input("Idade: "))
                nota = float(input("Nota: "))

                if idade < 0:
                    print("Idade inválida!")
                    continue

                if nota < 0 or nota > 10:
                    print("Nota deve ser entre 0 e 10!")
                    continue

                ficha = {
                    "nome": nome,
                    "idade": idade,
                    "nota": nota
                }

                alunos.append(ficha)
                print("Aluno cadastrado!")
                break

            except ValueError:
                print("Digite valores válidos! ")




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
    while True:

        if len(alunos) > 0:
            nomeProcurado = input("Nome para busca: ").strip().lower()

            if nomeProcurado != "":
                encontrado = False
                for i in alunos:
                    if nomeProcurado == i['nome']:
                        print("")
                        print(f"""
                        Nome: {i['nome']}
                        Idade: {i['idade']}
                        Nota: {i['nota']}
                        """)
                        encontrado = True

                if not encontrado:
                    print("Aluno não encontrado.")

            else:
                print("Digite um nome, por favor!")
                break
        else:
            print("Lista vazia, busca impossível.")
            break
        break

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


