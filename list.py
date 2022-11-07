from functions import ler_alunos
from env_ambient import quant

def list():
    alunos = ler_alunos()
    for aluno in alunos:
        print("id:",alunos[aluno][0])
        print("nome:",alunos[aluno][1])
        print("matricula:",alunos[aluno][2])
        print("id:",alunos[aluno][3])
        print("nota:",alunos[aluno][4])