# Input

# Será 1 entrada principal:
# Um inteiro “n” informando quantos números serão convertidos
# Após isso teremos n entradas com as seguintes informações
# Uma string informando a operação (Conversão) a ser realizada
# DEC : Binário → Decimal
# BIN : Decimal → Binário
# Uma entrada informando o valor a ser convertido (Sempre realize as operações a partir desse número)
# Uma entrada informando o palpite do jogador acerca da conversão

# Output

# Para os casos em que um palpite estiver errado
# Palpite Incorreto, o valor {numero} = {resultado_correto}
# Ao final do programa, caso a quantidade de acertos seja maior que 50%
# Bazinga! Quem realizou esses cálculos foi o computador??
# Caso, a quantidade de acertos seja menor
# Parece que realizar conversões em binário não é o seu forte


rounds = int(input())
score = 0

for i in range (rounds):
    type = input() 
    result_int = 0
    result_str = ""
    power = 0
    length = 0

    if (type == "DEC"): 
        binary = input()
        guess = int(input())
        for element in (binary): 
            length += 1
        j = length - 1
        for element in (binary):
            result_int +=  (int(element) * (2**j))
            j -= 1
        
        if (guess == result_int):
            score += 1
        else:
            print(f"Palpite Incorreto, o valor {binary} = {result_int}")

    elif (type == "BIN"): 
        decimal = int(input())
        guess = input()
        decimal_storage = decimal

        
        while (decimal_storage > 0):
            if (decimal_storage % 2 == 0):
                decimal_storage = decimal_storage / 2
                power += 1
            else:
                decimal_storage -= 1

       
        decimal_storage2 = decimal
        for y in range (power, -1, -1):
                if (decimal_storage2 >= (2**y)):
                    result_str = (result_str + "1") 
                    decimal_storage2 -= (2**y)
                elif (decimal_storage2  < 2**y):
                    result_str = (result_str + "0")
  
        
        if (guess == result_str):
            score += 1
        else:
            print(f"Palpite Incorreto, o valor {decimal} = {result_str}")

if ((score / rounds) > 0.5): 
    print("Bazinga! Quem realizou esses cálculos foi o computador??")
else: 
    print("Parece que realizar conversões em binário não é o seu forte")