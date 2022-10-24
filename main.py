from menu import menu
from create import criar

NOME_DATABASE = "database.csv"
alunos = []

def salvar_arq():
    with open(NOME_DATABASE,"w") as arq:
        sep = arq.readline() # Lendo primeira linhas
        variaveis = arq.readline() # Lendo segunda linha  
        arq.writelines((sep,"\n"))
        arq.writelines((variaveis,"\n"))
        for i in range((len(arq.readlines()))):
            aluno = ';'.join(alunos[i])
            arq.writelines((aluno,"\n"))
            
    
def main():
    escolha = menu()
    if escolha == "+":
        aluno = criar()
        
salvar_arq()