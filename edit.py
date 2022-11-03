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
            alunos[i][4] = input("Escreva a nova nota:")
    salvar_arq(alunos)