# Input

# Você receberá uma string m que determinará qual operação deve ser realizada, em seguida receberá um inteiro x que vai indicar com quantos números a operação será realizada, depois seguem-se x linhas com os valores que devem ser utilizados.
# Por fim, você receberá um valor para determinar se haverá uma nova operação ou não, se o valor for diferente de 1, significa que o programa chegou ao fim.
# A string m para indicar a operação segue o padrão abaixo:
# Para a soma: S
# Para a subtração: sub
# Para multiplicação: M
# Para a divisão: D
# Exemplo:
# D -> definindo que a operação será divisão
# 3 -> quantidade de números que serão operados
# 1 } -> operandos
# 2 } -> operandos
# 3 } -> operandos
# 0 -> Indicador que não haverá outra operação

# Output

# Ao fim de cada operação você deve printar o resultado final

def soma(list):
    resultado = 0
    for operador in lista_de_operadores:
        resultado += operador
    print(resultado) 
def subtracao(list):
    resultado = lista_de_operadores[0]
    for i in range (1, (total_operadores)):
        resultado -= lista_de_operadores[i]
    print(resultado) 
def multiplicacao(list):
    resultado = lista_de_operadores[0]
    for i in range (1, (total_operadores)):
        resultado =  (resultado * (lista_de_operadores[i]))
    print(resultado) 
def divisao(list):
    resultado = lista_de_operadores[0]
    for i in range (1, total_operadores):
        resultado = (resultado / (lista_de_operadores[i]))
    print(resultado) 

proxima_operacao = 1
while (proxima_operacao == 1):
    qual_operador = input()
    total_operadores = int(input())
    lista_de_operadores = []
    for i in range (total_operadores):
        operador = int(input())
        lista_de_operadores.append(operador)
    if (qual_operador == "S"):
        soma(lista_de_operadores)
    elif (qual_operador == "sub"):
        subtracao(lista_de_operadores)
    elif (qual_operador == "M"):
        multiplicacao(lista_de_operadores)
    elif (qual_operador == "D"):
        divisao(lista_de_operadores)
    proxima_operacao = int(input())