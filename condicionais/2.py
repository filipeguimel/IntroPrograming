# Input

# O input é uma linha única contendo o nome da comida a ser identificada, que pode ser uma das abaixo:
# “Pamonha”
# “Canjica”
# “Bolo de milho”

# Output

# Se a comida escolhida for canjica, deverá retornar:
# “Boa! Canjica faz parte.”
# Se a comida escolhida for pamonha, deverá retornar:
# “Boa! Pamonha faz parte.”
# Se a comida escolhida for bolo de milho, deverá retornar:
# “Boa! Bolo de milho faz parte.”
# Caso, outro tipo de comida for digitada ou qualquer outra coisa que não seja os 3 tipos, irá retornar:
# “Opa! Parece que voce procura um tipo de comida que nao combina com essa epoca, tente novamente.”

comida=str(input())
if comida=="Pamonha":
  print("Boa! Pamonha faz parte.")
elif comida=="Canjica":
  print("Boa! Canjica faz parte.")
elif comida=="Bolo de milho":
  print("Boa! Bolo de milho faz parte.")
else:
  print("Opa! Parece que voce procura um tipo de comida que nao combina com essa epoca, tente novamente.")