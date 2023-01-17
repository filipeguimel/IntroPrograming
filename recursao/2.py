# Input

# Para avaliar a capacidade do seu código, Clank receberá um inteiro N que indica a quantidade de sentenças que serão recebidas.
# N
# Em seguida, você receberá N sentenças matemáticas;
# exp1
# exp2
# ...
# expN

# Output

# Para cada entrada, você deverá retornar se há uma igualdade na quantidade de parênteses, o código deverá apresentar as seguintes respostas:
# → Se a quantidade de parênteses '(' for igual a quantidade de parênteses ')':
# “Essa sentença está com os parênteses balanceados, HOORAY!”
# →Se a quantidade de parênteses '(' for maior que a quantidade de parênteses ')':
# ”A quantidade de parênteses '(' está maior que a de ')', vamos descartá-la”
# →Se a quantidade de parênteses ')' for maior que a quantidade de parênteses '(':
# ”A quantidade de parênteses ')' está maior que a de '(', vamos descartá-la”
# Obs.: para printar aspas dentro da função print, você pode digitar ** (contra-barra) + ' (aspa) junto ou colocar como aspas mais externas as aspas duplas "

def parenteses_abertos(expressao, aberto):
    if aberto in expressao:
        expressao.remove(aberto)
        return parenteses_abertos(expressao, aberto) + 1
    else: 
        return 0

def parenteses_fechados(expressao, fechado):
    if fechado in expressao:
        expressao.remove(fechado)
        return parenteses_fechados(expressao, fechado) + 1
    else: 
        return 0

aberto = '('
fechado = ')'

rodadas = int(input())
for rodada in range(rodadas):

    expressao = list(input())

    prntss_abertos = parenteses_abertos(expressao, aberto)
    prntss_fechados = parenteses_fechados(expressao, fechado)

    if (prntss_abertos == prntss_fechados):
        print('Essa sentença está com os parênteses balanceados, HOORAY!')
    elif (prntss_abertos > prntss_fechados):
        print("A quantidade de parênteses '(' está maior que a de ')', vamos descartá-la")
    elif (prntss_fechados > prntss_abertos):
        print("A quantidade de parênteses ')' está maior que a de '(', vamos descartá-la")