from menu import menu
from create import criar
from delete import deletar
from edit import editar
from functions import salvar_arq

def main():
    escolha = menu()
    if escolha == "1":
        criar()
    elif escolha == "4":
        editar()
    elif escolha == "5":
        deletar()
while True:
    main()