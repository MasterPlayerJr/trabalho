NOME_DATABASE = "database.csv"
NOME_ARQ_ID = "ultimo_id.txt"
with open(NOME_ARQ_ID,'r') as arq:
    ultimo_id = int(arq.read())