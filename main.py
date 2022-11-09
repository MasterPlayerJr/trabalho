from menu import menu
from create import criar
from delete import deletar
from edit import editar
from calc_mean import media
from list_id import list_id
from lista import lista

def main():
    while True:
        escolha = menu()
        if escolha == 1:
            criar()
        elif escolha == 2:
            lista()
        elif escolha == 3:
            list_id()
        elif escolha == 4:
            editar()
        elif escolha == 5:
            deletar()
        elif escolha == 6:
            media()
        elif escolha == 0:
            break

main()