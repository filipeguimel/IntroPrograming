# Input

# O programa deverá receber um inteiro inicial que representa a quantidade de pedras lançadas por cada um.
# N
# Seguido de 2 sequências de N inteiros separados por espaço.
# X1 … XN
# Y1 … YN

# Output

# Se as duas listas forem iguais, mesmo que em ordem diferente, imprima:
# “Dale Gohan!”
# E, caso não sejam, imprima:
# "Ih, nao foi agora, Gohan! Vamos tentar de novo semana que vem."

rodadas = int(input())
gohan = [int(x) for x in input().split(" ")]
piccolo = [int(x) for x in input().split(" ")]
vitorias = 0
piccolo_dicionario = {}
gohan_dicionario = {}
keyerror = False
for number in piccolo:
    if (number not in piccolo_dicionario.keys()):
        piccolo_dicionario.update({number : 1})
    else:
        piccolo_dicionario[number] += 1
for number in gohan:
    if (number not in gohan_dicionario.keys()):
        gohan_dicionario.update({number : 1})
    else:
        gohan_dicionario[number] += 1

for key in piccolo_dicionario.keys():
    try:
        if (piccolo_dicionario[key] == gohan_dicionario[key]):
            vitorias += 1
    except KeyError:
        keyerror = True
if (vitorias == len(piccolo_dicionario)):
    print("Dale Gohan!")
elif (vitorias != len(piccolo_dicionario or keyerror)):
    print("Ih, nao foi agora, Gohan! Vamos tentar de novo semana que vem.")