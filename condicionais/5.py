# Input

# Serão 4 linhas de input:
# nome do fogo de artificio
# quantidade de decibeis dos fogos de felipe
# quantidade de decibeis máxima em Caruaru
# quantidade de decibeis máxima em Campina Grande

# Output

# Caso os fogos de artifício de Felipe possam ser comercializados em ambas as cidades, essa mensagem aparecerá:
# “Boa Felipe, o {nome_do_fogo} será um sucesso em Campina Grande e Caruaru!”
# Caso apenas em Caruaru o show poderá ser feito:
# “Infelizmente em Campina Grande não vai rolar, mas em Caruaru o {nome_do_fogo} vai ser extouro!”
# Caso apenas em Campina Grande possa ser feito:
# “Infelizmente em Caruaru não vai rolar, mas em Campina Grande o {nome_do_fogo} vai ser extouro!”
# Caso em nenhum dos municípios seja liberado:
# “Poxa Felipe, não vai ser dessa vez que {nome_do_fogo} fará um sucesso pelas festas juninas do Brasil”

fogo=str(input())
decibeis_felipe=int(input())
decibeis_caruaru=int(input())
decibeis_campina=int(input())

if decibeis_campina>decibeis_felipe and decibeis_caruaru>decibeis_felipe:
  print(f"Boa Felipe, o {fogo} será um sucesso em Campina Grande e Caruaru!")
elif decibeis_felipe>decibeis_campina and decibeis_caruaru>decibeis_felipe:
  print(f"Infelizmente em Campina Grande não vai rolar, mas em Caruaru o {fogo} vai ser extouro!")
elif decibeis_felipe>decibeis_caruaru and decibeis_campina>decibeis_felipe:
  print(f"Infelizmente em Caruaru não vai rolar, mas em Campina Grande o {fogo} vai ser extouro!")
else:
  print(f'Poxa Felipe, não vai ser dessa vez que {fogo} fará um sucesso pelas festas juninas do Brasil')