# Cada número representa uma letra, de acordo com algumas regras:
# De 0 até 49, os números representam letras minúsculas, de forma que 0 = a, 1 = b, etc. Lembre-se que deve-se considerar que o alfabeto inicia novamente da letra a para números maiores que 25. Ex. 25 = z e 26 = a.
# De 50 até 99, os números representam letras maiúsculas, de forma que 50 = A, 51 = B, etc. Lembre-se que deve-se considerar que o alfabeto inicia novamente da letra A para números maiores que 75. Ex. 75 = Z e 76 = A.
# Se o número for 100, ele representa um espaço para separar duas palavras.
# Se algum número não estiver no intervalo identificado pelas regras acima, não é possível traduzi-lo.
# AS PALAVRAS NÃO TÊM ACENTO E NEM Ç
# Você pode usar os métodos do python ord() e chr() e deve consultar a Tabela Ascii para usar essas funções corretamente. Também lembre de construir uma função para traduzir os números.

# Input

# Você receberá uma lista de x números inteiros separada por espaço:
# n1 n2 n3 n4 n5 n6 .... nx

# Output

# A saída deve conter a mensagem que você e Haru conseguiram decodificar, caso não seja possível fazer a decodificação completa, a mensagem deve ser a seguinte:
# 'Infelizmente os números nao dizem nada'

def decode (code):
    code_list = code.split(" ")
    fail = False
    message_temp = ""
    for number in code_list:
        i = code_list.index(number)
        code_list[i] = int(number)
        number = code_list[i]
        
        if (number >= 50 and number <= 99): 
            if (number <= 75): 
                number_ascii = number + 15
            elif (number >= 76): 
                number_ascii = number - 11
        elif (number >= 0 and number <= 49):
            if (number <= 25): 
                number_ascii = number + 97
            elif (number >= 26 and number <= 49): 
                number_ascii = number + 71
        elif (number == 100):
            number_ascii = 32
        elif (number < 0 or number > 100):
            fail = True
        
        message_temp = message_temp + (chr(number_ascii))
    
    if (fail):
        message_decoded = "Infelizmente os números nao dizem nada"
    else: 
        message_decoded = message_temp
    return message_decoded

code = input()
message_decoded = decode(code)

print(message_decoded)