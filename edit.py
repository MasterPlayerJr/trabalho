from env_ambient import quant_linhas
from functions import ler_alunos, salvar_arq, limpar
from random import randint

def editar():
    limpar(0)
    alunos = ler_alunos()
    escolha = input("Escolha o id do aluno a editar:")
    found = False
    for i in range(0,quant_linhas - 2):
        if int(alunos[i][0]) == int(escolha):
            found = True
            alunos[i][1] = input("Escreva o nome:")
            alunos[i][3] = input("Informe a idade:")
            while True:
                if int(alunos[i][3]) < 0:
                    alunos[i][3] = int(input("Idade invalida! Digite novamente:"))
                else:
                    break
            alunos[i][4] = int(input("Escreva a nova nota:"))
            while True:
                if int(alunos[i][3]) < 0 or int(alunos[i][3]) > 100:
                    alunos[i][3] = int(input("Idade invalida! Digite novamente:"))
                else:
                    break
    if not found:
        print("Aluno não encontrado!")
    else:
        print("Sucesso ao editar aluno!")
    input()