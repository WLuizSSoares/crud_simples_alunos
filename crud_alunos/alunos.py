def cadastrar_aluno(alunos):
        """Interage com o usuário para cadastrar um aluno e o adiciona à lista.

        A função solicita nome, idade e nota via terminal, valida os ados e insere o
        dicionário aluno diretamente na lista fornecida.

        Args:
            alunos (list): A lista onde o dicionário do aluno é inserido.

        Note:
            Esta função altera a lista 'alunos' in-place e não possui retorno.

        """

        while True:
            try:
                nome = input("Nome: ").strip().lower()
                idade = int(input("Idade: "))
                nota = float(input("Nota: "))

                if idade < 1:
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
    """Exibe um menu com as opções do sistema."""
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
    """Exibe na tela os dados de todos os alunos cadastrados na lista.

        A função percorre a lista de alunos e formata a exibição de cada registro no terminal.
        Se a lista estiver vazia, exibe mensagem de alerta.

        Args:
            alunos (list): A lista onde estão armazenados os dados para exibição
    """
    if not alunos:
        print("Lista está vazia!!")
    else:
        for i in alunos:
            print(f"""
            ---------------------
            Nome: {i['nome']}
            Idade: {i['idade']}
            Nota: {i['nota']}
            ---------------------""")


def buscar_aluno(alunos):
    """Busca e exibe os dados de um aluno pelo nome.

    A função interage com o usuário para obter o nome do aluno, realiza a
    busca na lista fornecida e imprime os dados se encontrados. Caso a lista
    esteja vazia ou o aluno não exista, exibe mensagens de aviso.

    Args:
        alunos (list): A lista de dicionários onde a busca será realizada.
    """
    while True:
        if len(alunos) > 0:
            nome_procurado = input("Nome para busca: ").strip().lower()

            if nome_procurado != "":
                encontrado = False
                for i in alunos:
                    if nome_procurado == i['nome']:
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
    nome_alterar = input("Nome para alteração: ").strip().lower()
    encontrado = False
    for i in alunos:
        if nome_alterar == i['nome']:
            nova_nota = float(input("Nova nota: "))
            i['nota'] = nova_nota
            encontrado = True
            print("Nota alterada com sucesso!")
            break
    if not encontrado:
        print("Aluno não encontrado")


def remover_aluno(alunos):
    nome_remover = input("Nome para remoção: ").strip().lower()
    encontrado = False
    for i in alunos:
        if nome_remover == i['nome']:
            alunos.remove(i)
            encontrado = True
            print("Aluno removido com sucesso!")
            break
    if not encontrado:
        print("Aluno não encontrado!")


