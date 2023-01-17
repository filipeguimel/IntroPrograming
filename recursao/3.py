# Input

# O programa receberá uma string S com o formato especificado no enunciado da questão.
# S

# Output

# Caso CHAR, a letra presente no nome da dimensão, seja maiúscula, o programa deverá imprimir a seguinte mensagem:
# Morty!!! Morty!!! Vamos para a dimensão {NOME DA DIMENSÃO}, Morty!!! Vai ser legal, Morty!!! Rick e Morty na dimensão {NOME DA DIMENSÃO} para sempre, Morty!!! Wubba lubba dub dub!!!
# Caso contrário:
# Oh geez, Rick!!! Eu não sei se ir pra dimensão {NOME DA DIMENSÃO} é uma boa ideia... Eu estou com medo, Rick!!! Oh geez!!!

def ftrl(vlr):
    if vlr > 1:
        return vlr * ftrl(vlr - 1)
    else:
        return 1
def cmbnc_smpls(maior): 
    vlr = maior
    global k_ftrl
    k_ftrl = ftrl(vlr)
    vlr = n
    global n_ftrl
    n_ftrl  = ftrl(vlr)
    vlr = n-maior
    global n_menos_k_ftrl
    n_menos_k_ftrl = ftrl(vlr)
    global num
    num = int(n_ftrl/(k_ftrl*n_menos_k_ftrl))
    return num
ltrs = input()
maiu = []
minu = []
for ltr in ltrs: 
    if ltr.isupper():
        maiu.append(ltr)
    else:
        minu.append(ltr)
if len(maiu) >= len(minu): 
    maior = len(maiu)
    lst_maior = maiu 
else:
    maior = len(minu)
    lst_maior = minu 
k_ftrl = 0
n_ftrl = 0
n_menos_k_ftrl = 0
n = len(ltrs)
num = 0
cmbnc_smpls(maior)
r = num % maior
crctr = lst_maior[r]
nome = f'{crctr}-{num}'
if crctr.isupper():
    print(f'Morty!!! Morty!!! Vamos para a dimensão {nome}, Morty!!! Vai ser legal, Morty!!! Rick e Morty na dimensão {nome} para sempre, Morty!!! Wubba lubba dub dub!!!')
else:
    print(f'Oh geez, Rick!!! Eu não sei se ir pra dimensão {nome} é uma boa ideia... Eu estou com medo, Rick!!! Oh geez!!!')