from functions import limpar

def menu():
    limpar(0)
    while True:
        print(" == Matricula == ")
        print("1 - Cadastro de Aluno")
        print("2 - Listar Todos os Alunos")
        print("3 - Listar Aluno em Especifico")
        print("4 - Atualizar Aluno")
        print("5 - Excluir Aluno")
        print("6 - Media do Aluno")
        print("0 - Sair")
        escolha = input("")
        return escolha 