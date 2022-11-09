from functions import limpar,ler_alunos,salvar_arq

def deletar():
    fechar = False
    while not fechar:
        limpar(0)
        alunos = ler_alunos()
        print(" == Deletar Aluno ==")
        escolha_id = input("Escolha o id a ser deletado:")
        for aluno in alunos:
            if aluno[0] != escolha_id:
                print("Id do aluno inexistente")
                break

        for i in range((len(alunos))):
            if alunos[i][0] == escolha_id:
                alunos.pop(i)
                salvar_arq(alunos)
                fechar = True
        input("Sucesso ao deletar aluno!")
