# Input

# O primeiro input será o nome de quem está enviando as listas com os filmes, sendo Bonna ou João:
# nome = Nome do dono da lista.
# O segundo, será a quantidade de filmes e notas que as listas possuem:
# quantidade = Quantidade de filmes e notas.
# Após isso, seu programa irá receber os nomes e as notas respectivamente, no formato:
# {nome_filme} - {nota_filme}
# OBS: você deve usar .split() para tratar as entradas

# Output

# Caso a dona da lista seja Bonna, você deverá printar a mensagem:
# "Os filmes sugeridos por Bonna são:”
# Caso o dono da lista seja João, você deverá printar a mensagem:
# "Os filmes sugeridos por João são:”
# Após isso, você deverá printar a lista com os filmes e as notas no seguinte formato:
# {filme} - {nota}

nome=input()
quantidade=int(input())
contador=0
filmes=[]
notas=[]

while contador < quantidade:
  entrada=input()
  entrada_tratada=entrada.split('-')
  filmes.append(entrada_tratada[0])
  notas.append(entrada_tratada[1])
  contador+=1


print(filmes)