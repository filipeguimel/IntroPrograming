# Input

# A entrada consiste nas seguintes 6 linhas:
# "nome_da_quadrilha"
# "passo_1"
# "passo_2"
# "passo_3"
# "passo_4"
# "passo_5"
# Atenção: As entradas sempre serão amigáveis e nunca uma quadrilha será composta de apenas um único movimento.

# Output

# Se a pontuação for zero, deverá retornar a seguinte frase:
# "Poxa, [nome_da_quadrilha]. Por utilizarem de algum passo não permitido vocês tiveram a pontuação zerada."
# Caso a pontuação seja maior que zero:
# "Parabéns, [nome_da_quadrilha]! Bela apresentação. A pontuação foi de [pontuacao]!"
# Atenção: A pontuação deverá ser impressa com a precisão de 1 casa decimal.

nome=str(input())
passo1=str(input())
passo2=str(input())
passo3=str(input())
passo4=str(input())
passo5=str(input())

pontuação=float(0)
pontuação=0
passo_ilegal=False
teve_casamento=False
#passo1

if passo1=='Cumprimento':
  pontuação=pontuação+100
elif passo1=='Balancê':
  pontuação=pontuação+50
elif passo1=='Passeio':
  pontuação=pontuação+70
elif passo1=='Túnel':
  pontuação=pontuação*0.90
elif passo1=='Serrote':
  pontuação=pontuação+100
elif passo1=='Casamento':
  teve_casamento=True
elif passo1=='Despedida':
  pontuação=pontuação
else:
  passo_ilegal=True
  
#passo2

if passo2=='Cumprimento':
  pontuação=pontuação+10
elif passo2=='Balancê':
  pontuação=pontuação+50
elif passo2=='Passeio':
  pontuação=pontuação+70
elif passo2=='Túnel':
  pontuação=pontuação*0.90
elif passo2=='Serrote':
  pontuação=pontuação+100
elif passo2=='Casamento':
  teve_casamento=True
elif passo2=='Despedida':
  pontuação=pontuação
else:
  passo_ilegal=True
  
#passo3

if passo3=='Cumprimento':
  pontuação=pontuação+10
elif passo3=='Balancê':
  pontuação=pontuação+50
elif passo3=='Passeio':
  pontuação=pontuação+70
elif passo3=='Túnel':
  pontuação=pontuação*0.90
elif passo3=='Serrote':
  pontuação=pontuação+100
elif passo3=='Casamento':
  teve_casamento=True
elif passo3=='Despedida':
  pontuação=pontuação
else:
  passo_ilegal=True
  
#passo4

if passo4=='Cumprimento':
  pontuação=pontuação+10
elif passo4=='Balancê':
  pontuação=pontuação+50
elif passo4=='Passeio':
  pontuação=pontuação+70
elif passo4=='Túnel':
  pontuação=pontuação*0.90
elif passo4=='Serrote':
  pontuação=pontuação+100
elif passo4=='Casamento':
  teve_casamento=True
elif passo4=='Despedida':
  pontuação=pontuação
else:
  passo_ilegal=True
  
#passo5

if passo5=='Cumprimento':
  pontuação=pontuação+10
elif passo5=='Balancê':
  pontuação=pontuação+50
elif passo5=='Passeio':
  pontuação=pontuação+70
elif passo5=='Túnel':
  pontuação=pontuação*0.90
elif passo5=='Serrote':
  pontuação=pontuação+100
elif passo5=='Casamento':
  teve_casamento=True
elif passo5=='Despedida':
  pontuação=pontuação+35
else:
  passo_ilegal=True
  
if teve_casamento==True:
  pontuação=pontuação*2
if passo_ilegal==True:
  pontuação=0

if pontuação==0:
  print(f"Poxa, {nome}. Por utilizarem de algum passo não permitido vocês tiveram a pontuação zerada.")
elif pontuação>0:
  print(f'Parabéns, {nome}! Bela apresentação. A pontuação foi de {pontuação:.1f}!')
  

  

