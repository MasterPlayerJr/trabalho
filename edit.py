from env_ambient import quant_linhas
from functions import ler_alunos
from random import randint

def editar():
    alunos = ler_alunos()
    escolha = int(input("Escolha o id do aluno a editar:"))
    for i in range(0,quant_linhas):
        if int(alunos[i][0]) == escolha:
            aluno = alunos.pop(i)
            aluno[1] = input("Escreva o nome:")
            aluno[2] = randint(1,100000)
            aluno[3] = input("Informe a idade:")
            aluno[4] = input("Escreva a nova nota:")

            

editar()