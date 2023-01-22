# Input

# Você receberá a quantidade de estrelas
# N: Quantidade de estrelas
# Em seguida, receberá o eixo x seguido pelo eixo_y de cada N estrela.
# star1_x: Eixo X da estrela 1
# star1_y: Eixo Y da estrela 1
# star2_x: Eixo X da estrela 2
# star2_y: Eixo Y da estrela 2
# starN_x: Eixo X da estrela N
# starN_y: Eixo Y da estrela N
# Os eixos da localização das estrelas serão sempre maior que zero.

# Output

# Para cada distância calculada, você deve imprimir
# Distância [star{a} <-> star{b}]: {dist}
# Sendo a e b as posições das estrelas na ordem de entrada, começando a contagem apartir de 1 e dist a distância euclidiana transformada em inteiro entre as duas estrelas
# Ao final das entradas, seu código deve ser capaz de retornar corretamente o inteiro de cada distância e uma das 5 saídas possíveis. Se cair em uma das duas últimas condições, você não precisará imprimir as distâncias.
# Se todas as distâncias pertencerem à sequência de Fibonacci mas a soma das disâncias não for um número primo:
# Yes! Eu consegui!
# Se todas as distâncias pertencerem à sequência de Fibonacci e a soma das distâncias for um número primo
# Oh my god! Eu vou ganhar o Nobel primeiro que Sheldon!
# Se apenas uma das distâncias não pertencer a sequência:
# Oh, não! Eu quase consegui!
# Se duas ou mais distâncias não pertencerem à sequência e a soma das distâncias não for um número primo:
# Eu vou acabar como o Stuart :/
# Se duas ou mais distâncias não pertencerem à sequência mas a soma das distâncias for um número primo:
# Pelo menos o programa está funcionando...
# Se N for menor ou igual a 0
# Isso está quebrado, acho que Howard pode me ajudar.
# Se N for menor que 3 e maior que zero
# Acho que bebi demais, eu juro que tinha mais estrelas!

qtd_estrelas = int(input())
if qtd_estrelas <= 0:
    print('Isso está quebrado, acho que Howard pode me ajudar.')
elif 3 > qtd_estrelas > 0:
    print('Acho que bebi demais, eu juro que tinha mais estrelas!')
else:
    a = 1
    b = 2
    soma_dist = 0
    cont_nao_pertence = 0
    last_star_x = float(input())
    last_star_y = float(input())
    qtd_estrelas -= 1
    while qtd_estrelas != 0:
        star_x = float(input())
        star_y = float(input())
        dist = ((int(last_star_x) - int(star_x)) ** 2 + (int(last_star_y) - int(star_y)) ** 2) ** (1/2)
        print(f'Distância [star{a} <-> star{b}]: {int(dist)}')
        a += 1
        b += 1
        qtd_estrelas -= 1
        last_star_x = star_x
        last_star_y = star_y
        verificacao_fibonacci = 0
        nao_pertence = False
        num_anterior = 0
        num_posterior = 1
        while int(dist) >= verificacao_fibonacci:
            if int(dist) == verificacao_fibonacci:
                nao_pertence = False
            else:
                nao_pertence = True
            verificacao_fibonacci = num_anterior + num_posterior
            num_anterior = num_posterior
            num_posterior = verificacao_fibonacci
        if nao_pertence:
            cont_nao_pertence += 1
        soma_dist += int(dist)
    k = 1
    primo = False
    ocorrencia_primo = 0
    if soma_dist != 0 and soma_dist != 1:
        while k <= soma_dist:
            if soma_dist % k == 0:
                ocorrencia_primo += 1
            k += 1
        if ocorrencia_primo == 2:
            primo = True
        else:
            primo = False
    if cont_nao_pertence == 0:
        if not primo:
            print('Yes! Eu consegui!')
        else:
            print('Oh my god! Eu vou ganhar o Nobel primeiro que Sheldon!')
    elif cont_nao_pertence == 1:
        print('Oh, não! Eu quase consegui!')
    elif cont_nao_pertence >= 2:
        if not primo:
            print('Eu vou acabar como o Stuart :/')
        else:
            print('Pelo menos o programa está funcionando...')