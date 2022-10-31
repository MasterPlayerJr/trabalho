import os
from time import sleep
from env_ambient import NOME_DATABASE,ultimo_id

def limpar(tempo):
    sleep(tempo)
    os.system('cls' if os.name == 'nt' else 'clear')

def lista_str(lista):
    for i in range(len(lista)):
        lista[i] = str(lista[i])
    return lista

def salvar_arq(alunos_save):
    with open(NOME_DATABASE,"w") as arq:
        arq.writelines("sep=; \n")
        arq.writelines("id;nome;matricula;idade;nota \n")
        for i in range(0,len(alunos_save)):
            try:
                print(alunos_save)
                alunos_str = lista_str(alunos_save[i])
                alunos_str = ";".join(alunos_str)
                print(alunos_str)
                arq.writelines(f"{alunos_str}\n")
            except IndexError:
                continue

def ler_alunos():
    alunos = []
    with open(NOME_DATABASE,'r+') as arq:
        arq.readline()
        arq.readline()
        for i in range(0,ultimo_id):
            aluno = arq.readline().split(";")
            if aluno != '':
                if len(aluno) > 5:
                    aluno.pop()
                alunos.append(aluno)
    return alunos