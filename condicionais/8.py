# Input

# As entradas representam as informações de 3 cidades, para cada cidade, teremos uma string composta pelo nome da cidade, seguido da respectiva nota (0 <= nota <= 5.0, com 1 casa decimal) e a distância da cidade em relação ao usuário em km,
# Cidade 1
# Nota 1
# Distância 1
# Cidade 2
# Nota 2
# Distância 2
# Cidade 3
# Nota 3
# Distância 3

# Output

# A saída consiste de uma linha única
# Caso nenhuma cidade tenha nota maior ou igual a 4:
# Nota mínima não atingida
# Caso contrário, você deve imprimir a cidade com a maior pontuação
# Nome_Cidade

cidade1=str(input())
nota1=float(input()) 
distancia1=int(input())
cidade2=str(input())
nota2=float(input())
distancia2=int(input())
cidade3=str(input())
nota3=float(input())
distancia3=int(input())

if nota1<4 and nota2<4 and nota3<4:
  print('Nota mínima não atingida')
elif nota1>nota2 and nota1>nota3:
  print(cidade1)
elif nota2>nota1 and nota2>nota3:
  print(cidade2)
elif nota3>nota1 and nota3>nota2:
  print(cidade3)
elif nota1==nota2==nota3:
  if distancia1<distancia2 and distancia1<distancia3:
    print(cidade1)
  elif distancia2<distancia1 and distancia2<distancia3:
    print(cidade2)
  elif distancia3<distancia1 and distancia3<distancia2:
    print(cidade3)
   

