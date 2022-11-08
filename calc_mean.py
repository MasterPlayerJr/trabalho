from functions import ler_alunos,limpar
from env_ambient import quant_linhas

limpar(0)
def media():
    notas = []
    alunos = ler_alunos()
    for i in range(0,quant_linhas -2):
        nota = alunos[i][4]
        if nota[-1] == "\n":
            nota = nota[0:-1]
        notas.append(float(nota))
    print(notas)
    quant_notas = len(notas)
    soma = sum(notas)
    print(soma)
    media = soma / quant_notas
    print("A media de notas è", media)

media()