import os
from time import sleep

def limpar(tempo):
    sleep(tempo)
    os.system('cls' if os.name == 'nt' else 'clear')

def lista_str(lista):
    for i in range(len(lista)):
        lista[i] = str(lista[i])
    return lista