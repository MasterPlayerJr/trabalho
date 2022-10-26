from env_ambient import alunos
from functions import limpar

def deletar():
    fechar = False
    while not fechar:
        limpar(0)
        print(" == Deletar Aluno ==")
        escolha_id = input("Escolha o id a ser deletado:")
        for i in range(len(alunos)):
            if alunos[i][0] == escolha_id:
                alunos.pop(i)
                fechar = True
    return alunos