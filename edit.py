from env_ambient import quant_linhas
from functions import ler_alunos, salvar_arq
from random import randint

def editar():
    alunos = ler_alunos()
    escolha = int(input("Escolha o id do aluno a editar:"))
    for i in range(0,quant_linhas - 2):
        if int(alunos[i][0]) == escolha:
            alunos[i][1] = input("Escreva o nome:")
            alunos[i][2] = randint(1,100000)
            alunos[i][3] = input("Informe a idade:")
            while True:
                if alunos[i][3] < 0:
                    alunos[i][3] = int(input("Idade invalida! Digite novamente:"))
                else:
                    break
            alunos[i][4] = int(input("Escreva a nova nota:"))
            while True:
                if alunos[i][3] < 0 or alunos[i][3] > 100:
                    alunos[i][3] = int(input("Idade invalida! Digite novamente:"))
                else:
                    break
    salvar_arq(alunos)

editar()