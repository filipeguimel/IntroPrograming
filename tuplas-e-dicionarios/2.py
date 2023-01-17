# Input

# O Input terá duas linhas:
# A primeira será uma lista de inteiros que representa o número dos companheiros do Kuroko
# [p1, p2 ... px]
# A segunda será o número alvo que deve ser obtido ao somar o número de 2 companheiros
# target

# Output

# Uma lista com a posição dos dois companheiros, em ordem crescente, na lista de input
# [pos_companheiro1, pos_companheiro2]

jogadores = input()
alvo = int(input())

jogadores = jogadores.replace("[", "")
jogadores = jogadores.replace("]", "")
posicao_jogadores = [int(x) for x in jogadores.split(",")]
dicionario = {}
result = []
for i in range (len(posicao_jogadores)):
    dicionario[i] = posicao_jogadores[i] 
for key in dicionario.keys():
    for i in range (1, len(posicao_jogadores)):
        if ((key + i) < len(posicao_jogadores)):
            n1 = dicionario[key]
            n2 = dicionario[key+1]
            if ((dicionario[key] + dicionario[key+i]) == alvo):
                result = [key, key+i]
print(result)