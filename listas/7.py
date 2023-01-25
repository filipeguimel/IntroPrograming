nomes = []
qtds = []

total_zumbis = int(input())

qtd_frascos = int(input())

for i in range(qtd_frascos):
  nome, elementos = input().split()
  elementos = int(elementos)
  nomes.append(nome)
  qtds.append(elementos)

selecionados_nomes = []
selecionados_qtds = []

resultado = False

for i in range(qtd_frascos):
  selecionados_nomes.append(nomes[i])
  selecionados_qtds.append(qtds[i])
  while sum(selecionados_qtds) > total_zumbis:
    selecionados_nomes.pop(0)
    selecionados_qtds.pop(0)
  if sum(selecionados_qtds) == total_zumbis:
    resultado = True
    break

if resultado:
  print(f"Vencemos a batalha e a humanidade foi restaurada! {' '.join(selecionados_nomes)} foram usados para deszumbificar")
else:
  print("Estou sentido algo estranho... será que também vou virar zumbi?")