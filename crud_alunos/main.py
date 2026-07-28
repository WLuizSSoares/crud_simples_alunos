import alunos

list_alunos = []
while True:
    alunos.menu()
    opcao = int(input("Opção desejada: "))
    if opcao == 1:
        alunos.cadastrar_aluno(list_alunos)
    elif opcao == 2:
        alunos.listar_alunos(list_alunos)
    elif opcao == 3:
        alunos.buscar_aluno(list_alunos)
    elif opcao == 4:
        alunos.alterar_nota(list_alunos)
    elif opcao == 5:
        alunos.remover_aluno(list_alunos)
    elif opcao == 6:
        print("Programa encerrado!")
        break
    else:
        print("Opção inválida")
