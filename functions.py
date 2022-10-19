import os
from time import sleep

def limpar(tempo):
    sleep(tempo)
    os.system('cls' if os.name == 'nt' else 'clear')
