from functions import ler_alunos,limpar
from env_ambient import quant_linhas

def list_id():
    limpar(0)
    control = 0
    alunos = ler_alunos()
    escolha = int(input("Escolha um id:"))
    for i in range(0,quant_linhas -2):
        if int(alunos[i][0]) == escolha:
            print("id:",alunos[i][0])
            print("nome:",alunos[i][1])
            print("matricula:",alunos[i][2])
            print("idade:",alunos[i][3])
            print("nota:",alunos[i][4])
            control = 1

    if control == 0:
        print("Aluno não existente!")
    input()