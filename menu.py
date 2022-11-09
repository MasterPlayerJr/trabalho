from functions import limpar

def menu():
    while True:
        limpar(0)
        print(" == Matricula == ")
        print("1 - Cadastro de Aluno")
        print("2 - Listar Todos os Alunos")
        print("3 - Listar Aluno em Especifico")
        print("4 - Atualizar Aluno")
        print("5 - Excluir Aluno")
        print("6 - Media do Aluno")
        print("0 - Sair")
        escolha = input("Escolha uma opcao:")

        if escolha.isdigit():
            escolha = int(escolha)
            if escolha >= 0 and escolha <= 6:
                return escolha
                break