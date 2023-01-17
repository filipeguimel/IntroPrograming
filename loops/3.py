# Input

# A primeira entrada corresponde ao número do local do mapa que se deseja chegar (o ponto de partida é sempre considerado zero):
# X
# Em seguida, o programa receberá um número indefinido de inteiros positivos que correspondem ao progresso do participante na prova, indicando sua posição atual no mapa, sempre terminando com um número negativo (o número negativo não deve ser considerado no calculo do progresso):
# W
# Y
# Z
# ...
# Para cada entrada, deve-se somar ao progresso os valores de 1 até o inteiro da entrada (incluso). Por exemplo, se o inteiro for 5, você deve somar 1+2+3+4+5 à pontuação que indica a posição atual do participante.

# Output

# Ao final das entradas, uma das 5 possíveis saídas deve ser imprimida.
# Se o número do local atual for menor que o da desejada:
# Ainda falta um pouco...
# No caso do número atual ser igual ao do objetivo:
# Parabéns!!! Você é o mais inteligente
# O número atual sendo maior que o objetivo mas menor que 20 vezes ele:
# Parece que o gêniozinho passou um pouco do local...
# Se estiver de 20 à 100 vezes (incluindo 100) maior que a do objetivo:
# Acho que sua grande inteligência fez você se perder um pouco no caminho, onde estamos?
# Por fim, se o número atual for maior que 100 vezes a desejada:
# Hum... acho que o gêniozinho não tem mesmo doutorado ein...

destino=int(input())
progresso=0
posicao_atual=0
posicao_final=0
while progresso>=0:
  progresso=int(input())
  if progresso>0:
    posicao_atual=sum(range(1,progresso+1))
    posicao_final=posicao_final+posicao_atual
  elif progresso<0:
    break

if posicao_final<destino:
  print('Ainda falta um pouco...')
elif posicao_final==destino:
  print('Parabéns!!! Você é o mais inteligente')
elif posicao_final>destino and posicao_final<20*destino:
  print('Parece que o gêniozinho passou um pouco do local...')
elif 100*destino>=posicao_final>20*destino:
  print('Acho que sua grande inteligência fez você se perder um pouco no caminho, onde estamos?')
elif 100*destino<posicao_final:
  print('Hum... acho que o gêniozinho não tem mesmo doutorado ein...')