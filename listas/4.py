# Input

# Primeiramente, Jigsaw quer que você encontre as palavras escondidas na sala, portanto, a entrada terá 10 palavras da seguinte forma:
# palavra_1
# palavra_2
# palavra_3
# .
# palavra_10

# Output

# Em seguida, você procederá para cumprir os 2 desafios:
# Passo 1:
# Inicialmente, Jigsaw quer que você informe a ele todas as strings que não se repetiram da lista de strings que você encontrou. A saída deverá ser da seguinte maneira:
# As palavras sao: palavra_que_nao_repete_1 . . . palavra_que_nao_repete_k
# OBS: Entretanto, como seu notebook não tem todas as bibliotecas de python instaladas, você não poderá utilizar o método count() ou qualquer outra função pré-definida para isso.
# Passo 2:
# Após isso, Jigsaw disse que você deve fazer a soma do tamanho das palavras da lista desconsiderando aquelas que se repetem. Você deve então printar a soma desses valores.
# A soma do tamanho das palavras é: {soma_das_palavras}
# Ao final de tudo, Jigsaw deve dizer:
# Estou impressionado, você me venceu, pode ir embora...

palavras=[]

palavras_que_nao_se_repetem=[]
for i in range(10):
  palavra=input()
  palavras.append(palavra)


if palavras[0]!=palavras[1] and palavras[0]!=palavras[2] and palavras[0]!=palavras[3] and palavras[0]!=palavras[4] and palavras[0]!=palavras[5] and palavras[0]!=palavras[6] and palavras[0]!=palavras[7] and palavras[0]!=palavras[8] and palavras[0]!=palavras[9]:
  palavras_que_nao_se_repetem.append(palavras[0])
if palavras[1]!=palavras[0] and palavras[1]!=palavras[2] and palavras[1]!=palavras[3] and palavras[1]!=palavras[4] and palavras[1]!=palavras[5] and palavras[1]!=palavras[6] and palavras[1]!=palavras[7] and palavras[1]!=palavras[8] and palavras[1]!=palavras[9]:
  palavras_que_nao_se_repetem.append(palavras[1])
if palavras[2]!=palavras[0] and palavras[2]!=palavras[1] and palavras[2]!=palavras[3] and palavras[2]!=palavras[4] and palavras[2]!=palavras[5] and palavras[2]!=palavras[6] and palavras[2]!=palavras[7] and palavras[2]!=palavras[8] and palavras[2]!=palavras[9]:
  palavras_que_nao_se_repetem.append(palavras[2])
if palavras[3]!=palavras[0] and palavras[3]!=palavras[1] and palavras[3]!=palavras[2] and palavras[3]!=palavras[4] and palavras[3]!=palavras[5] and palavras[3]!=palavras[6] and palavras[3]!=palavras[7] and palavras[3]!=palavras[8] and palavras[3]!=palavras[9]:
  palavras_que_nao_se_repetem.append(palavras[3])
if palavras[4]!=palavras[0] and palavras[4]!=palavras[1] and palavras[4]!=palavras[2] and palavras[4]!=palavras[3] and palavras[4]!=palavras[5] and palavras[4]!=palavras[6] and palavras[4]!=palavras[7] and palavras[4]!=palavras[8] and palavras[4]!=palavras[9]:
  palavras_que_nao_se_repetem.append(palavras[4])
if palavras[5]!=palavras[0] and palavras[5]!=palavras[1] and palavras[5]!=palavras[2] and palavras[5]!=palavras[3] and palavras[5]!=palavras[4] and palavras[5]!=palavras[6] and palavras[5]!=palavras[7] and palavras[5]!=palavras[8] and palavras[5]!=palavras[9]:
  palavras_que_nao_se_repetem.append(palavras[5])
if palavras[6]!=palavras[0] and palavras[6]!=palavras[1] and palavras[6]!=palavras[2] and palavras[6]!=palavras[3] and palavras[6]!=palavras[4] and palavras[6]!=palavras[5] and palavras[6]!=palavras[7] and palavras[6]!=palavras[8] and palavras[6]!=palavras[9]:
  palavras_que_nao_se_repetem.append(palavras[6])
if palavras[7]!=palavras[0] and palavras[7]!=palavras[1] and palavras[7]!=palavras[2] and palavras[7]!=palavras[3] and palavras[7]!=palavras[4] and palavras[7]!=palavras[5] and palavras[7]!=palavras[6] and palavras[7]!=palavras[8] and palavras[7]!=palavras[9]:
  palavras_que_nao_se_repetem.append(palavras[7])
if palavras[8]!=palavras[0] and palavras[8]!=palavras[1] and palavras[8]!=palavras[2] and palavras[8]!=palavras[3] and palavras[8]!=palavras[4] and palavras[8]!=palavras[5] and palavras[8]!=palavras[6] and palavras[8]!=palavras[7] and palavras[8]!=palavras[9]:
  palavras_que_nao_se_repetem.append(palavras[8])
if palavras[9]!=palavras[0] and palavras[9]!=palavras[1] and palavras[9]!=palavras[2] and palavras[9]!=palavras[3] and palavras[9]!=palavras[4] and palavras[9]!=palavras[5] and palavras[9]!=palavras[6] and palavras[9]!=palavras[7] and palavras[9]!=palavras[8]:
  palavras_que_nao_se_repetem.append(palavras[9])

soma=0
print('As palavras sao:')
for x in range(len(palavras_que_nao_se_repetem)):
    print (palavras_que_nao_se_repetem[x])
    soma += len(palavras_que_nao_se_repetem[x])
    
print(f'A soma do tamanho das palavras é: {soma}')
print('Estou impressionado, você me venceu, pode ir embora...')


