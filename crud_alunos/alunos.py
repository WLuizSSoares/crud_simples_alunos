def ler_nome(mensagem):
    while True:
        nome = input(mensagem).strip().lower()
        if nome == "":
            print("Espaço vazio, digite um nome válido!")
            continue
        return nome
def ler_nota(mensagem):
    while True:
        try:
            nota = float(input(mensagem))

            if nota < 0 or nota > 10:
                print("Nota deve ser entre 0 e 10!")
                continue
            return nota
        except ValueError:
            print("Nota inválida! ")

def ler_idade(mensagem):
    while True:
        try:
            idade = int(input(mensagem))
            if idade < 0:
                print("Idade não pode ser negativa")
                continue

            return idade
        except ValueError:
            print("Idade inválida")

def buscar_por_nome(alunos, nome):
    for i in alunos:
        if nome == i["nome"]:
            return i
    return None

def exibir_aluno(aluno):
    print(f"""
        Nome: {aluno['nome']}
        Idade: {aluno['idade']}
        Nota: {aluno['nota']}
        """)



def cadastrar_aluno(alunos):
        """Interage com o usuário para cadastrar um aluno e o adiciona à lista.

        A função solicita nome, idade e nota via terminal, valida os ados e insere o
        dicionário aluno diretamente na lista fornecida.

        Args:
            alunos (list): A lista onde o dicionário do aluno é inserido.

        Note:
            Esta função altera a lista 'alunos' in-place e não possui retorno.

        """

        nome = ler_nome("Nome: ")
        idade = ler_idade("Idade: ")
        nota = ler_nota("Nota: ")

        ficha = {
            "nome": nome,
            "idade": idade,
            "nota": nota
        }

        alunos.append(ficha)
        print("Aluno cadastrado!")



def menu():
    """Exibe um menu com as opções do sistema."""
    print("""
    =============================
        Sistema Escolar V_2.0
    =============================

    1 - Cadastrar aluno
    2 - Listar alunos
    3 - Buscar aluno
    4 - Alterar nota
    5 - Remover aluno
    6 - Outras opções
    7 - Sair
    """)


def listar_alunos(alunos):
    """Exibe na tela os dados de todos os alunos cadastrados na lista.

        A função percorre a lista de alunos e formata a exibição de cada registro no terminal.
        Se a lista estiver vazia, exibe mensagem de alerta.

        Args:
            alunos (list): A lista onde estão armazenados os dados para exibição
    """
    if alunos:
        for i in alunos:
            exibir_aluno(i)
    else:
        print("Nenhum aluno cadastrado")


def buscar_aluno(alunos):
    """Busca e exibe os dados de um aluno pelo nome.

    A função interage com o usuário para obter o nome do aluno, realiza a
    busca na lista fornecida e imprime os dados se encontrados. Caso a lista
    esteja vazia ou o aluno não exista, exibe mensagens de aviso.

    Args:
        alunos (list): A lista de dicionários onde a busca será realizada.
    """

    nome_procurado = ler_nome("Nome para busca: ")
    aluno = buscar_por_nome(alunos, nome_procurado)

    if aluno:
        exibir_aluno(aluno)
    else:
        print("Nenhum aluno cadastrado!")

def alterar_nota(alunos):
    """Busca um aluno pelo nome e altera a nota de um aluno.

    Solicita ao usuário o nome do aluno, procura o registro na lista
    informada e, quando encontrado, solicita a nova nota e atualiza o
    valor armazenado. Caso o aluno não seja encontrado, exibe uma
    mensagem informativa.

    Args:
        alunos(list): Lista de dicionários onde contém os alunos para alteração
    Returns:
         None
    """
    nome_alterar = ler_nome("Nome para alteração: ")
    aluno = buscar_por_nome(alunos, nome_alterar)
    if aluno:
        nova_nota = float(input("Nova nota: "))
        aluno['nota'] = nova_nota
        print("Nota alterada com sucesso!")
    else:
        print("Aluno não encontrado.")


def remover_aluno(alunos):
    """
    Remove um aluno da lista pelo nome.

    Solicita ao usuário o nome do aluno, procura o registro na lista e,
    caso seja encontrado, remove o aluno. Se o aluno não existir, exibe
    uma mensagem informativa.

    Args:
        alunos (list): Lista de dicionários contendo os alunos cadastrados.

    Returns:
        None
    """
    nome_remover = ler_nome("Nome para remoção: ")
    aluno = buscar_por_nome(alunos, nome_remover)
    if aluno:
        alunos.remove(aluno)
        print("Aluno removido com sucesso!")
    else:
        print("Aluno não encontrado!")




