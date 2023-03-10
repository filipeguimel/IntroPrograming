def busca_binaria(lista, chave, rota):
    if len(lista) > 0:
        elemento_meio = lista[len(lista) // 2]
    if len(lista) == 1:
        rota += 'Meio'
        if lista[0] == chave:
            return rota, True
        else:
            return rota, False
    elif len(lista) == 0:
        rota += 'Meio'
        return rota, False
    elif elemento_meio == chave:
        rota = 'Meio'
        return rota, True
    else:
        if elemento_meio > chave:
            rota += 'Esquerda -> '
            return busca_binaria(lista[0:len(lista) // 2], chave, rota)
        elif elemento_meio < chave:
            rota += 'Direita -> '
            return busca_binaria(lista[(len(lista) // 2) + 1:len(lista)], chave, rota)
        else:
            return busca_binaria([elemento_meio], chave, rota)
def transf_binario(numero):
    resultado = ''
    valor_inicial = int(numero)
    quociente = valor_inicial
    if valor_inicial == 0 or valor_inicial == 1:
        resultado = valor_inicial
        resultado = str(resultado)
    else:
        while quociente != 1:
            resto = quociente % 2
            quociente = quociente // 2
            if quociente != 1:
                resultado = str(resto) + resultado
            elif quociente == 1:
                resultado = str(quociente) + str(resto) + resultado
    return resultado
numeros_salas = input()
lista_analise_str = numeros_salas.split(' ')
lista_analise = []
for sala in lista_analise_str:
    lista_analise.append(int(sala))
numero_escolhido = int(input())
rota_busca, achou_numero = busca_binaria(lista_analise, numero_escolhido, '')
numero_escolhido_negativo = False
if numero_escolhido < 0:
    numero_escolhido_negativo = True
    numero_escolhido = 0 - numero_escolhido
numero_escolhido_str = str(numero_escolhido)
numero_escolhido_binario = transf_binario(numero_escolhido_str)
numero_bits = int(input())
if len(numero_escolhido_binario) > numero_bits:
    suporta_tamanho_bits = False
else:
    suporta_tamanho_bits = True
    while len(numero_escolhido_binario) != numero_bits:
        numero_escolhido_binario = '0' + numero_escolhido_binario
if achou_numero:
    if suporta_tamanho_bits:
        print(f'{rota_busca}, seguindo por essas coordenadas voc?? vai chegar no n??mero {numero_escolhido_binario}.')
    else:
        print('Consegui encontar a sa??da, mas n??o consigo falar pois o n??mero ?? muito grande para essa quantidade de bits.')
elif not achou_numero:
    if lista_analise[0] > numero_escolhido or numero_escolhido > lista_analise[-1] or numero_escolhido_negativo:
        print('Acho que a Doutora se confundiu, pois ?? imposs??vel chegar nesse n??mero pois ele ?? menor que a menor sala ou maior que o maior da sala.')
    else:
        if not suporta_tamanho_bits:
            print('Busquei muito, mas n??o achei a sala, que nem posso dizer, j?? que tenho poucos bits.')
        else:
            print(f'{rota_busca}, mas n??o consegui achar.')