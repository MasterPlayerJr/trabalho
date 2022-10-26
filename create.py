from random import randint
from functions import limpar
from env_ambient import NOME_ARQ_ID,NOME_DATABASE

def criar_id():
    with open(NOME_ARQ_ID,"r") as arq:
        id = int(arq.read()) + 1
    with open(NOME_ARQ_ID,"w") as arq:
        arq.write(str(id))
    return id

def criar():
    limpar(0)
    print(" == Criar Aluno == ")
    nome_escolha = input("Nome do Aluno:")
    matricula = randint(0,10000)
    idade = int(input("Idade do aluno:"))
    nota = float(input("Nota do aluno(0-100):"))
    id = criar_id()
    aluno = [id,nome_escolha,matricula,idade,nota]
    with open(NOME_DATABASE,'a') as arq:
        for i in aluno:
            arq.writelines(f"{i}")
        arq.write("\n")
    input("Sucesso ao criar aluno!")

criar()