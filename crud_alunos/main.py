import alunos
import persistencia

lista_alunos = persistencia.carregar_alunos()
while True:
    alunos.menu()
    opcao = int(input("Opção desejada: "))
    if opcao == 1:
        alunos.cadastrar_aluno(lista_alunos)
        persistencia.salvar_alunos(lista_alunos)
    elif opcao == 2:
        alunos.listar_alunos(lista_alunos)
    elif opcao == 3:
        alunos.buscar_aluno(lista_alunos)
    elif opcao == 4:
        alunos.alterar_nota(lista_alunos)
        persistencia.salvar_alunos(lista_alunos)
    elif opcao == 5:
        alunos.remover_aluno(lista_alunos)
        persistencia.salvar_alunos(lista_alunos)
    elif opcao == 6:
        print("Programa encerrado!")
        break
    else:
        print("Opção inválida")
