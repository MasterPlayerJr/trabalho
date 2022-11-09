from functions import limpar,ler_alunos,salvar_arq
from env_ambient import quant_linhas

def deletar():
    limpar(0)
    alunos = ler_alunos()
    print(" == Deletar Aluno ==")
    escolha_id = input("Escolha o id a ser deletado:")
    for i in range(quant_linhas - 2):
        if alunos[i][0] != escolha_id:
            print("Id do aluno inexistente!")
            break
    for i in range(quant_linhas - 2):
        if alunos[i][0] == escolha_id:
            alunos.pop(i)
            salvar_arq(alunos)
            break

deletar()