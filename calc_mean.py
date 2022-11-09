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
    quant_notas = len(notas)
    soma = sum(notas)
    media = soma / quant_notas
    input(f"A media de notas é de {media}")