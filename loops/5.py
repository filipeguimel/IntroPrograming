# Input

# As entradas do programa não têm uma quantidade definida e se encerram sempre com a frase “Fim do Show!”, como é ilustrado abaixo:
# piada_1
# reação_1
# piada_2
# reação_2
# ...
# piada_N
# reação_N
# Fim do Show!
# Caso ele tenha gostado, sua reação será unicamente um sonoro “BAZINGA!”. Em caso contrário, ele terá qualquer outra reação.

# Output

# Para a saída do programa, temos três opções.
# Se o número de piadas boas foi bastante superior:
# “BAZINGA! O senso de humor dele é muito bom, Amy, parece com o meu!”
# Se houve equilíbrio entre piadas boas e ruins:
# “Esse stand up foi bastante mediano, Amy. Parece a carreira do Leonard!”
# Já se o número de piadas ruins foi bastante superior:
# “Amy, acredito que acabei de perder 60 de QI ouvindo essas piadas!”
# Considere que para que um tipo de reação às piadas seja “bastante superior” ao outro, elas devem ser mais de 60% do total de reações. Caso contrário, há equilíbrio entre boas e ruins.

boa=0
ruim=0

while boa>=0 :
  piada=input()
  if piada=="Fim do Show!":
    break
  reacao=input()
  
  if reacao=='BAZINGA!':
    boa+=1
  else:
    ruim+=1

if boa>0.6*(boa+ruim):
  print('BAZINGA! O senso de humor dele é muito bom, Amy, parece com o meu!')
elif ruim>0.6*(boa+ruim):
  print('Amy, acredito que acabei de perder 60 de QI ouvindo essas piadas!')
else:
  print('Esse stand up foi bastante mediano, Amy. Parece a carreira do Leonard!')