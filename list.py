from env_ambient import NOME_DATABASE,ultimo_id

def ler_alunos():
    alunos = []
    with open(NOME_DATABASE,'r+') as arq:
        arq.readline()
        arq.readline()
        for i in range(0,ultimo_id):
            aluno = arq.readline().split(";")
            if len(aluno) > 5:
                aluno.pop()
            alunos.append(aluno)
    return alunos