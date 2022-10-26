NOME_DATABASE = "database.csv"
NOME_ARQ_ID = "ultimo_id.txt"
with open(NOME_ARQ_ID,'r') as arq:
    ultimo_id = int(arq.read())
    
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
            print(alunos)
            input()
    return alunos

alunos = ler_alunos()