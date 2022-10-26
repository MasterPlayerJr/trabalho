from menu import menu
from create import criar
from functions import lista_str
from delete import deletar
from env_ambient import ultimo_id,NOME_DATABASE,alunos

def salvar_arq(alunos_save):
    with open(NOME_DATABASE,"w") as arq:
        arq.writelines("sep=; \n")
        arq.writelines("id;nome;matricula;idade;nota")
        for i in range(0,ultimo_id + 1):
            try:
                alunos_str = lista_str(alunos_save[i])
                alunos_str = ";".join(alunos_str)
                arq.writelines(f"\n{alunos_str};")
                print("Deu")
                input()
            except IndexError:
                print("Erro")
                input()
                continue

       
def main():
    global alunos
    escolha = menu()
    if escolha == "1":
        aluno = criar()
        alunos.append(aluno)
        print(alunos)
        input()
        salvar_arq(alunos)
    elif escolha == "5":
        alunos = deletar()
        salvar_arq(alunos)
    elif escolha == "s":
        salvar_arq(alunos)

while True:
    main()