# Input

# Para o input, inicialmente, será recebida uma lista de nomes separados por vírgula, em uma mesma linha.
# nome1,nome2,nome3, ... ,nome n
# Em seguida, serão recebidas diversas entradas, até que sobre um único suspeito na lista e o mistério seja solucionado.
# Para cada entrada descrita abaixo, realize a operação correspondente:
# “Não encontrei nada no primeiro suspeito"
# Você deve remover o primeiro suspeito da lista.
# “O último da lista está limpo”
# Você deve remover o último suspeito da lista
# “Procurei por um elemento um pouco mais além na lista e ele está acima de qualquer suspeita”
# Você deve remover o nome do indivíduo que encontra-se no meio da lista.
# **OBS: Note que, caso o número de elementos restantes na lista seja par, deve-se remover o elemento de maior índice entre os dois elementos do meio.
# “Pelas minhas verificações, não encontrei nada de alarmante no indivíduo que está na seguinte posição:”
# Você receberá logo em seguida uma entrada com a posição do suspeito na lista, que começa no índice 0, e o removerá da lista.
# “Acho que temos mais uma opção a ser analisada…”
# Você receberá logo em seguida uma entrada com o nome do novo suspeito e o adicionará no final da lista.
# Qualquer outra entrada além das mencionadas anteriormente não gerará nenhuma operação na lista.
# **OBS: Está liberado o uso de métodos e funções prontas de listas

# Output

# Sempre que a entrada for diferente das especificadas no input, você avisará ao Dean:
# “Isso não estava no combinado, a lista vai permanecer do mesmo jeito”
# Quando a lista tiver apenas um suspeito, você deve finalizar as operações e avisar ao Dean que a busca chegou ao fim por meio da seguinte frase:
# “Acho que encontramos o suspeito. O seu nome é {nome_suspeito}, vamos salvar o Sam!”

nomes=input()
suspeitos=nomes.split(',')
#print(suspeitos)


while len(suspeitos) != 1:
    entrada=input()
    if entrada == "Não encontrei nada no primeiro suspeito":
        del suspeitos[0]
        #print(suspeitos)
        continue
    elif entrada == "O último da lista está limpo":
        del suspeitos[-1]
        #print(suspeitos)
        continue
    elif entrada == "Procurei por um elemento um pouco mais além na lista e ele está acima de qualquer suspeita":
        if len(suspeitos) % 2 == 0:
            del suspeitos[(int(len(suspeitos)/2))]
        else:
            del suspeitos[(int((len(suspeitos)-1)/2))]
        #print(suspeitos)
        continue
    elif entrada == "Pelas minhas verificações, não encontrei nada de alarmante no indivíduo que está na seguinte posição:":
        posicao=int(input())
        del suspeitos[posicao]
        #print(suspeitos)
        continue
    elif entrada == "Acho que temos mais uma opção a ser analisada…":
        novo_suspeito=input()
        suspeitos.append(novo_suspeito)
        #print(suspeitos)
        continue
    else:
        print('Isso não estava no combinado, a lista vai permanecer do mesmo jeito')
        continue

if len(suspeitos) == 1:
        print(f'Acho que encontramos o suspeito. O seu nome é {suspeitos[0]}, vamos salvar o Sam!')