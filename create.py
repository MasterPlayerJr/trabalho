from random import randint
from functions import limpar

NOME_ARQ_ID = "ultimo_id.txt"

def criar_id():
    with open(NOME_ARQ_ID,"r") as arq:
        id = int(arq.read()) + 1
    with open(NOME_ARQ_ID,"w") as arq:
        arq.write(str(id))
    return id

def criar():
    limpar(0)
    print(" == Criar Aluno == ")
    id = criar_id()
    nome_escolha = input("Nome do Aluno:")
    matricula = randint(0,10000)
    idade = int(input("Idade do aluno:"))
    nota = float(input("Nota do aluno (0-100):"))
    aluno = [id,nome_escolha,matricula,idade,nota]
