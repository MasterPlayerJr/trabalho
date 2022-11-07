import os
from time import sleep
from env_ambient import NOME_DATABASE,quant_linhas

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
        arq.writelines("id;nome;matricula;idade;nota")
        for i in range(0,len(alunos_save)):
            try:
                alunos_str = lista_str(alunos_save[i])
                alunos_str = ";".join(alunos_str)
                if alunos_str[-1] == "\n":
                    alunos_str = alunos_str[0:-1]
                arq.writelines(f"\n{alunos_str}")
            except IndexError:
                continue

def ler_alunos():
    alunos = []
    with open(NOME_DATABASE,'r+') as arq:
        arq.readline()
        arq.readline()
        for i in range(0,(quant_linhas - 2)):
            aluno = arq.readline().split(";")
            alunos.append(aluno)
    return alunos
