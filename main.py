from menu import menu
from create import criar
from delete import deletar
from functions import salvar_arq

def main():
    escolha = menu()
    if escolha == "1":
        alunos = criar()
    elif escolha == "5":
        alunos = deletar()
    elif escolha == "s":
        salvar_arq(alunos)

while True:
    main()