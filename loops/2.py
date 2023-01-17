# Input

# Você receberá indeterminadas entradas contendo ações realizadas pelo Sheldon para resolver a situação, até receber a entrada “parar”. As ações podem ser as seguintes:
# ir para o grad → Diminui a Temperatura em 5 graus e aumenta a Internet em 300mb/s
# sair para a rua → Aumenta a Temperatura em 5 graus
# comer uma quentinha → Acaba com a fome de Sheldon
# conectar no wifi → Aumenta a Internet em 100mb/s
# parar → Sempre será a última entrada

# Output

# Caso receba uma entrada inválida, imprima e continue o programa:
# Entrada inválida
# Ao final das N entradas, seu código deverá imprimir, na seguinte ordem:
# -Caso a temperatura seja de 30 graus ou superior:
# A temperatura aqui não está agradável
# -Caso a temperatura seja de 25 graus ou inferior:
# Agora sim, está aconchegante
# Caso Sheldon esteja com fome:
# Meu corpo precisa de comida
# -Caso a Internet esteja abaixo de 100mb/s:
# Essa conexão está horrível
# Por fim, independente das saídas anteriores, caso Sheldon esteja sem fome, a temperatura esteja de 25 graus ou inferior e a conexão seja igual ou maior 300mb/s, seu código deverá imprimir:
# Finalmente um lugar preciso para mim!

Temperatura = 30
Fome = True
Internet = 0

acao='a'

while acao!='parar':
  acao=str(input())
  if acao =='ir para o grad':
    Temperatura = Temperatura - 5
    Internet = Internet + 300
  elif acao =='sair para a rua':
    Temperatura = Temperatura + 5
  elif acao =='comer uma quentinha':
    Fome = False
  elif acao =='conectar no wifi':
    Internet = Internet + 100
  elif acao=='parar':
    break
  else:
    print('Entrada inválida')
  
if Temperatura>=30:
  print('A temperatura aqui não está agradável')
elif Temperatura<=25:
  print('Agora sim, está aconchegante')
if Fome==True:
  print('Meu corpo precisa de comida')
if Internet<100:
  print('Essa conexão está horrível')

if Fome==False and Temperatura<=25 and Internet>=300:
  print('Finalmente um lugar preciso para mim!')