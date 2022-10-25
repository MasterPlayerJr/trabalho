from menu import menu
from create import criar
from functions import lista_str
from delete import deletar
from list import ler_alunos
from env_ambient import ultimo_id,NOME_DATABASE

alunos = ler_alunos()

def salvar_arq():
    with open(NOME_DATABASE,"a") as arq:
        for i in range(0,ultimo_id):
            try:
                alunos_str = lista_str(alunos[i])
                alunos_str = ";".join(alunos_str)
                arq.writelines(f"\n{alunos_str}")
            except IndexError:
                continue
       
def main():
    escolha = menu()
    if escolha == "1":
        aluno = criar()
        alunos.append(aluno)
    elif escolha == "3":
        deletar()

while True:
    main()
    salvar_arq()