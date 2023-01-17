# a tarefa consiste em receber 3 números inteiros e em seguida calcular a soma dos dígitos de cada um dos números
# exemplo : 312 → somadigitos = 3 + 1 + 2 = 6
# Após fazer a soma dos dígitos de cada um, eles devem calcular o máximo divisor comum entre a soma dos dígitos de cada um dos 3 números, ajude as crianças a implementar um programa que realiza isso

# Input

# A entrada consiste de 3 números inteiros e positivos
# [num1]
# [num2]
# [num3]

# Output

# A saída consiste da frase
# O MDC obtido é: X
# Onde X é o MDC calculado

def soma_digitos(n):
    if (n == 0):
        return 0
    else:
        return (n % 10) + soma_digitos(n // 10) #o resto do número é o dígito mais a direita e a divisão inteira do número são os números restantes a serem somados

def mdc(a, b):
    if (b == 0):
        return a
    else:
        return mdc(b, a%b) 
for rodada in range(3):
    n = int(input())
    soma_digitos(n)
    if (rodada == 0):
        a = soma_digitos(n)
    elif (rodada == 1):
        b = soma_digitos(n)
    else:
        c = soma_digitos(n)

a = mdc(a, b)
b = c 
resultado = mdc(a, b)

print(f'O MDC obtido é: {resultado}')