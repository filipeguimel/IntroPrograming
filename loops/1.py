# Input

# A 1ª linha da entrada será um número “N”, esse número representa o total de rodadas. (N > 0)
# Após a primeira linha será dado as escolhas de Sheldon e Raj, cada um em uma linha e sempre nessa ordem. Isso irá se repetir N vezes.

# Exemplo:

# N
# escolha_sheldon1
# escolha_raj1
# …
# escolha_sheldonN
# escolha_rajN

# Output

# Ao final das rodadas você deve imprimir o seguinte:
# Caso Sheldon tenha ganhado mais partidas:
# "BAZINGA! EU SOU O SENHOR DA SALA!"
# Caso Raj tenha ganhado mais partidas:
# "ENGOLE ESSA, SHELDON!"
# Caso eles ganhem o mesmo número de partidas ou hajam apenas empates:
# "Oh não, precisamos de outra rodada."

rodadas=int(input())

rodada=1
shel_vit=0
raj_vit=0
empate=0
rodadas_ganhas_sheldon=0
rodadas_ganhas_raj=0
rodadas_empatadas=0

while rodada<rodadas:
  
  sheldon=str(input())
  raj=str(input())
  
  if sheldon=='lagarto' and raj=='spock':
    shel_vit+=1
  elif sheldon=='lagarto' and raj=='tesoura':
    raj_vit+=1
  elif sheldon=='lagarto' and raj=='lagarto':
    empate+=1
  elif sheldon=='spock' and raj=='lagarto':
    raj_vit+=1
  elif sheldon=='spock' and raj=='tesoura':
    shel_vit+=1
  elif sheldon=='spock' and raj=='spock':
    empate+=1
  elif sheldon=='tesoura' and raj=='spock':
    raj_vit+=1
  elif sheldon=='tesoura' and raj=='lagarto':
    shel_vit+=1
  elif sheldon=='tesoura' and raj=='tesoura':
    empate+=1
  
  if shel_vit==1:
    rodadas_ganhas_sheldon+=1
  elif raj_vit==1:
    rodadas_ganhas_raj+=1
  elif empate==1:
    rodadas_empatadas+=1
  
  rodada+=1
  
if rodadas_ganhas_sheldon>rodadas_ganhas_raj:
  print('BAZINGA! EU SOU O SENHOR DA SALA!')
elif rodadas_ganhas_raj>rodadas_ganhas_sheldon:
  print('ENGOLE ESSA, SHELDON!')
elif rodadas_ganhas_sheldon==rodadas_ganhas_raj:
  print('Oh não, precisamos de outra rodada.')
    