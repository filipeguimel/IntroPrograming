# Input

# O input possui uma quantidade indeterminada de linhas de entrada, mas sempre termina com a mensagem "Boa noite", quando o programa deve encerrar. As batidas do Sheldon sempre seguem o padrão "toc-toc-toc" seguido de "Penny", repetido três vezes, se esse padrão for interrompido então sabemos que não é o Sheldon e então a contagem deve recomeçar.
# Exemplo do padrão de Sheldon:
# toc-toc-toc
# Penny
# toc-toc-toc
# Penny
# toc-toc-toc
# Penny
# Boa noite

# Output

# Toda vez que o código receber um ‘toc-toc-toc’ e um ‘Penny’, deverá imprimir a contagem, começando em 1:
# 1
# 2
# 3
# Se a contagem chegar em 3, será o Sheldon, e deverá imprimir:
# Pode entrar Sheldon
# Se receber algum input que fora do padrão do Sheldon, interrompe a contagem e imprime:
# Não pode entrar, se identifique!!!
# Quando receber o Boa noite:
# Boa noite Penny

toc=0
penny=0

while toc>=0 :
  m=input()
  if m=="toc-toc-toc":
    toc+=1
    
  elif m=="Penny":
    penny+=1
    print(penny)
  elif m=="Boa noite":
    print("Boa noite Penny")
    break
  else:
    print("Não pode entrar, se identifique!!!")
    toc=penny=0
    
  if toc == 3 and penny == 3:
    print("Pode entrar Sheldon")
    toc=penny=0
  
  
