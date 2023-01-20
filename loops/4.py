# Input

# A primeira entrada indicará o número de planetas a serem comparados, você deve aguardar por um número inteiro válido, ou seja, que indique ao menos 2 planetas para serem comparados. Caso o número seja inválido, o programa deverá informar o usuário com a mensagem:
# Número inválido, tente novamente
# O programa deve então receber mais números até que se receba um número válido.
# n_invalido
# n_invalido
# ...
# n_invalido
# n_valido
# Em seguida, você receberá n informações de planetas, cada uma contendo uma string com o nome do planeta, um float r > 0 com o raio em Rearth, um float m > 0 com a massa em Mearth e um inteiro k > 0 com a temperatura em Kelvin para cada planeta.

# Output

# A saída consiste em uma das seguintes mensagens, contendo o planeta com o índice mais próximo de 1.
# Caso esse índice seja igual a 1, deverá ser printado:
# {nome} é perfeito!
# Se esse índice for menor que 1, deverá ser printado:
# {nome} vai dar pro gasto
# Caso o índice ultrapasse 1, deverá ser printado:
# {nome} vai ter que servir


quantidade_planetas=int(input())


while quantidade_planetas<2:
  print('Número inválido, tente novamente')
  quantidade_planetas=int(input())
melhor_indice=100
for quantidade_planetas in range (quantidade_planetas):
  planeta=str(input())
  raio=float(input())
  massa=float(input())
  temperatura=int(input())
  indice=((raio+massa+(temperatura/288))/3)
  
  
  if abs(indice - 1) < abs(melhor_indice - 1):
    melhor_indice=indice
    melhor_planeta=planeta
  
  
if melhor_indice==1:
  print(f'{melhor_planeta} é perfeito!')
elif melhor_indice<1:
  print(f'{melhor_planeta} vai dar pro gasto')
elif melhor_indice>1:
  print(f'{melhor_planeta} vai ter que servir')