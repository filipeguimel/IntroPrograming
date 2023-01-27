quantidade_de_cartas = int(input())
todas_as_cartas = []
for i in range (quantidade_de_cartas):
    card_temp= input().split(" ")
    defesa = card_temp.pop(-1)
    ataque = card_temp.pop(-1)
    nome = (" ").join(card_temp)
    carta = {'nome': nome, 'ataque': ataque, 'defesa': defesa}
    todas_as_cartas.append(carta)
todos_os_ataques = [] #criando listas com ataques e defesas
todas_as_defesas = []
for i in range (quantidade_de_cartas):
    todos_os_ataques.append(int(todas_as_cartas[i]['ataque']))
    todas_as_defesas.append(int(todas_as_cartas[i]['defesa']))
ataque_maximo = max(todos_os_ataques) # máximo de cada e pega a posição na lista
index_do_ataque = todos_os_ataques.index(ataque_maximo)
defesa_maxima = max(todas_as_defesas)
index_da_defesa = todas_as_defesas.index(defesa_maxima)
# tupla pra diminuir as respostas
winner = ( todas_as_cartas[index_do_ataque]['nome'], todas_as_cartas[index_do_ataque]['ataque'],  todas_as_cartas[index_da_defesa]['nome'], todas_as_cartas[index_da_defesa]['defesa'], todas_as_cartas[index_da_defesa]['defesa'])
print(f"Carta com maior poder de ataque: {(winner[0])}\nAtaque: {(winner[1])}\n\nCarta com maior poder de defesa: {(winner[2])}\nDefesa: {(winner[3])}")