# Input

# A entrada compreende várias linhas de código, contendo, cada uma o nome do aluno e os sintomas que apresentou separados por vírgula e um espaço como no exemplo abaixo:
# nome_1, sintoma_1, sintoma_2, sintoma_3, (...), sintoma_n
# nome_2, sintoma_1, sintoma_2, sintoma_3, (...), sintoma_n
# ...
# nome_n, sintoma_1, sintoma_2, sintoma_3, (...), sintoma_n
# descobrir
# Sendo "descobrir" a última entrada antes de obter os resultados.
# Obs.: o nome dos sintomas deve sempre ser escrito sem acento gráfico e sem o cedilha.

# Output

# Se não conseguirmos encontrar nenhum aluno com TODOS os 5 sintomas apresentados, seu programa deverá printar:
# "Não conseguimos encontrar ninguém com esses sintomas, o próximo ataque do Vecna será imprevisível."
# Caso Max tenha apresentado TODOS os sintomas, a saída deverá ser:
# "Oh não, Max está em perigo! Let's run up that hill com a Kate Bush e ajudar nossa amiga."
# Caso Max não seja a única com TODOS os sintomas, a mensagem abaixo deve ser printada:
# "Além dela, tem mais {n} pessoa(s) na mira do Vecna!"
# Porém, se Max não aparecer na entrada ou não tiver TODOS os 5 sintomas, a saída será:
# "Tem {n} pessoa(s) na mira do Vecna!"
# E por último, além das mensagens a cima, se houver mais de uma pessoa em perigo:
# "Precisamos avisar {nome_1}, {nome_2}, ... e {nome_n} para prepararem suas músicas favoritas."
# ou, se só houver uma pessoa:
# "Precisamos avisar {nome_n} para preparar sua música favorita."
# Onde {n} é a quantidade de pessoas que apresentaram os sintomas e {nome_n} o nome delas.
# Obs.: O nome da Max não deve aparecer na última mensagem (sendo uma ou mais pessoas).

descobrir = False
pessoas_e_sintomas=[]
while descobrir == False:
  entrada=input()
  if entrada == 'descobrir':
    break
  else:
    pessoas_e_sintomas.append(entrada)
pessoa1=(pessoas_e_sintomas[0])
pessoa2=(pessoas_e_sintomas[1])
sintomas_pessoa1=pessoa1.split(',')
del sintomas_pessoa1[0]

sintomas=['dor de cabeça', 'insônia', 'pesadelos', 'suor frio', 'visões']
if sintomas_pessoa1[0] in sintomas:
  print("sim")


