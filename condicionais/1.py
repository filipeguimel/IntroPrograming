# Input

# Você receberá um número inteiro:
# numero (int)

# Output

# Se for número 1 imprima: “Você tirou o Doguinho! Vai receber muitos lambeijos!”
# Se for o número 2: “Gabriel Queiroz, eu escolho você! Aí vem o galã da monitoria te tascar um beijão!”
# Se for número 3: “Que azar! Não vai beijar ninguém! Tome uma língua de gato de prêmio de consolação…”
# Se for número 4: “Olha só! O misterioso monitor de branco vem te entregar uma lista para fazer e um selinho de encorajamento!”
# Se for número 5: “Ca-Calegário?!!! Ganhou um Hi-5 e um projeto de IP/P1 para entregar daqui a duas semanas!”
# Se digitar qualquer outro número: “Véi! São 5 opções, não é difícil escolher…”

n=int(input())

if n==1:
  print('Você tirou o Doguinho! Vai receber muitos lambeijos!')
elif n==2:
  print('Gabriel Queiroz, eu escolho você! Aí vem o galã da monitoria te tascar um beijão!')
elif n==3:
  print('Que azar! Não vai beijar ninguém! Tome uma língua de gato de prêmio de consolação…')
elif n==4:
  print('Olha só! O misterioso monitor de branco vem te entregar uma lista para fazer e um selinho de encorajamento!')
elif n==5:
  print('Ca-Calegário?!!! Ganhou um Hi-5 e um projeto de IP/P1 para entregar daqui a duas semanas!')
else:
  print('Véi! São 5 opções, não é difícil escolher…')