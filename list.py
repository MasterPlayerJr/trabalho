from functions import ler_alunos,limpar
from env_ambient import quant_linhas

limpar(0)
def list():
    alunos = ler_alunos()
    for i in range(0,quant_linhas -2):
        print("id:",alunos[i][0])
        print("nome:",alunos[i][1])
        print("matricula:",alunos[i][2])
        print("idade:",alunos[i][3])
        print("nota:",alunos[i][4])

list()