# Input

# As primeiras n entradas (n > 0) serão as transmissões que você interceptará ao longo do tempo; elas poderão vir do Mar Podre ou dos aviões estrangeiros, ambos podendo ser potenciais ameaças ao pacífico Vale do Vento. A última entrada será uma entrada que não apresentou barulhos que você consegue identificar.
# entrada_1
# entrada_2
# entrada_3
# ….
# entrada_n

# Output

# Para cada entrada, você irá dizer, a partir das informações dadas, se as transmissões são das criaturas do Mar Podre, de aeronaves de outros países, ou se ambos os sinais estão se misturando, e para cada entrada, o código deverá apresentar as seguintes respostas:
# Se apenas padrões das criaturas forem captados:
# “É apenas o Mar Podre se comunicando, podemos ficar tranquilos, por enquanto…”
# Se apenas padrões dos aviões forem captados:
# “São sinais de aeronaves estrangeiras! Devemos preparar nossas defesas??”
# Se ambos padrões forem captados em uma única transmissão:
# “A transmissão sugere que tropas estrangeiras e as criaturas do Mar Podre irão se confrontar! Precisamos impedi-los antes que mais mortes desnecessárias ocorram!”
# Quando nenhum padrão for captado, o código deverá printar essa mensagem e se encerrar:
# “Não é possível determinar a origem da transmissão… Isso deverá levar mais algum tempo.”

def find_source1 (transmission):
    insect_count = 0
    insect = False
    dirty_sea = ["crcrcrcrcr", "uuuuuuuoooooo", "ooooooeeeeeeee"]
    for word in dirty_sea:
        if (word in transmission):
            insect_count += 1
    if (insect_count > 0):
        insect = True
    return insect
def find_source2 (transmission):
    foreing_count = 0
    foreing = False
    foreign_aircraft = ["ppprrrrrooon", "tutututututututu", "eeeeeeeeoooooo"]
    for word in foreign_aircraft:
        if (word in transmission):
            foreing_count += 1 
    if (foreing_count > 0):
        foreing = True
    return foreing
            
next = True
while (next):
    transmission = input().split(" ")
    insect = find_source1(transmission)
    foreing = find_source2(transmission)
    if (insect and foreing):
        print("A transmissão sugere que tropas estrangeiras e as criaturas do Mar Podre irão se confrontar! Precisamos impedi-los antes que mais mortes desnecessárias ocorram!")
    elif (insect):
        print("É apenas o Mar Podre se comunicando, podemos ficar tranquilos, por enquanto…")
    elif (foreing):
        print("São sinais de aeronaves estrangeiras! Devemos preparar nossas defesas??")
    else:
        print("Não é possível determinar a origem da transmissão… Isso deverá levar mais algum tempo.")
        next = False