# Input

# A linha de entrada será um número inteiro, O dia que Pedro irá consultar o valor máximo que ele pode gastar.
# X - inteiro

# Output

# A linha de saída será uma string, que dependerá da linha de entrada digitada por Pedro.
# Caso for escolhido um dia que um dos cantores favoritos de Pedro cantará, deverá retornar: “Um de seus cantores favoritos cantará nesse dia, portanto gaste até, no máximo, 400 reais!”
# Caso for escolhido um dia que nenhum cantor favorito de Pedro cantará, deverá retornar: “Nenhum cantor favorito seu cantará nesse dia, portanto gaste até, no máximo, 200 reais!”
# Caso for escolhido um dia que seja fora do intervalo do dia 17 ao dia 26, deverá retornar: “Você escolheu um dia que não irá acontecer nenhum show, tente novamente!”
# Caso for escolhido o dia 20, também deverá retornar: “Você escolheu um dia que não irá acontecer nenhum show, tente novamente!”

dia=int(input())

if dia==18:
  print("Um de seus cantores favoritos cantará nesse dia, portanto gaste até, no máximo, 400 reais!")
elif dia==22:
  print("Um de seus cantores favoritos cantará nesse dia, portanto gaste até, no máximo, 400 reais!")
elif dia==24:
  print("Um de seus cantores favoritos cantará nesse dia, portanto gaste até, no máximo, 400 reais!")
elif dia==26:
  print("Um de seus cantores favoritos cantará nesse dia, portanto gaste até, no máximo, 400 reais!")
elif dia==17:
  print("Nenhum cantor favorito seu cantará nesse dia, portanto gaste até, no máximo, 200 reais!")
elif dia==19:
  print("Nenhum cantor favorito seu cantará nesse dia, portanto gaste até, no máximo, 200 reais!")
elif dia==21:
  print("Nenhum cantor favorito seu cantará nesse dia, portanto gaste até, no máximo, 200 reais!")
elif dia==23:
  print("Nenhum cantor favorito seu cantará nesse dia, portanto gaste até, no máximo, 200 reais!")
elif dia==25:
  print("Nenhum cantor favorito seu cantará nesse dia, portanto gaste até, no máximo, 200 reais!")
elif dia==20:
  print("Você escolheu um dia que não irá acontecer nenhum show, tente novamente!")
else:
  print("Você escolheu um dia que não irá acontecer nenhum show, tente novamente!")