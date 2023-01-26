def letra_numero(letra):
    global posicao
    letras = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    posicao = letras.index(letra) 
    return posicao

def numero_letra(valor):
    letras = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    return letras[valor] 

def mod_letra(posicao):
    global mod
    mod = posicao % 11
    return mod

def fatorial(mod): 
    if (mod > 1):
        return (mod) * fatorial(mod - 1)
    elif (mod >= 0):
        return 1

def fibonacci(mod):
    if mod <= 1:
        return mod
    else:
        return fibonacci(mod - 1) + fibonacci(mod - 2)

posicao = 0
lista_fibonacci = []
lista_fatorial = []
senha_final = []
senhas_finais = []
numeros_sem_conversao = []
pedaco_convertido = []
existe_senha = False

senha = input()
quantidade = int(input())
for palavras in range(quantidade):
    palavra = input()
    for letra in palavra:
        letra_numero(letra) 
        mod_letra(posicao) 

        for i in range(mod): 
            lista_fibonacci.append(fibonacci(i))
            lista_fatorial.append(fatorial(i))

        if mod == 0:
            senha_final.append('1')
        elif mod % 2 != 0:
            for x in range(len(lista_fibonacci)):
                numeros_sem_conversao.append(lista_fibonacci[x] * lista_fatorial[x]) 
        else:
            for x in range(len(lista_fibonacci)):
                numeros_sem_conversao.append(lista_fibonacci[x] + lista_fatorial[x]) 

        for valor in numeros_sem_conversao:
            pedaco_convertido.append(numero_letra(valor % 26)) 
        senha_final.append(('').join(pedaco_convertido)) 

        lista_fatorial = [] 
        lista_fibonacci = []
        pedaco_convertido = []
        numeros_sem_conversao = []
    senhas_finais.append(('').join(senha_final)) 
    if senhas_finais[0] == senha:
        existe_senha = True
    senha_final = [] 
    senhas_finais = []

if existe_senha:
    print('Achamos! Achamos a senha.')
else:
    print('É... Temos que procurar mais.')