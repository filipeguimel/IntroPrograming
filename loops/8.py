# Input

# A primeira entrada é a quantidade de instruções que será enviada em uma string binária com 4 bits.
# 0001 (1) ≤ qnt_instrucoes ≤ 0100 (4)
# Em seguida, será recebido o tipo de corpo que esta sendo observado, pode haver três tipos de entrada:
# 0101 → planeta
# 1101 → galáxia
# 0000 → buraco negro supermassivo
# Se a instrução seja indicando um planeta:
# O programa reconhece qual será o conteúdo e será recebida uma descrição seguido de um valor, podendo ser:
# “Beleza”
# 0 ou 1
# “Possibilidade de vida extraterrestre”
# 0 ou 1
# “Agua aparente”
# 0 ou 1
# "Temperatura adequada"
# 0 ou 1
# "Quantidade de luas"
# 0001 (1) ≤ qnt_luas ≤ 0011 (3)
# End
# 1 → afirmação
# 0 → negação
# Se for indicando uma galáxia:
# Sempre terá duas entradas:
# qnt_planetas_em_milhoes
# A quantidade de planetas em cada galáxia está restrita a três quantias:
# 01100100 ⇒ 100 em decimal
# 11001000 ⇒ 200 em decimal
# 100101100 ⇒ 300 em decimal
# buraco_super
# Podendo ter dois valores:
# 0 ⇒ indicando que não há buraco negro supermassivo nessa galáxia
# 1 ⇒ indicando que há
# Se for indicando um buraco negro:
# Sempre terá três entradas:
# massa em bilhões de massas solares
# Na analise foi observado três valores significantes que se repetem:
# 0101 ⇒ 5 em binário
# 1010 ⇒ 10 em binário
# 1111 ⇒ 15 em binário
# spin (rotação)
# 0 ou 1
# carga
# Pode haver três tipos:
# 0000 ⇒ Carga neutra
# 0001 ⇒ Carga positiva
# e se não for nenhuma das anteriores ⇒ Carga negativa

# Output

# Caso a instrução seja indicando um planeta:
# Se apresentar agua aparente, tempetatura adequada, beleza e vida extraterrestre:
# "Achamos o planeta ideal e ainda tem {qnt_lua} lua(s)!"
# "Parece bom demais pra ser verdade, que tipo de vida sera que nos aguarda?"
# Se apresentar agua aparente, tempetatura adequada, beleza e não haver vida extraterrestre:
# "Ainda nao sabemos se o planeta e habitavel, parece nao haver vida"
# Se apresentar agua aparente, tempetatura adequada, vida extraterrestre, mas não for bonito:
# "O planeta e possivelmente habitavel porem olha essa aparencia, mesmo que tenha {qnt_lua} lua(s) vamos omitir esse do relatorio!"
# Caso não seja incluído em nenhuma das sentenças anteriores:
# "Vish! Esse nao satisfaz nem as condicoes basicas, nao perderemos tempo"
# Caso seja indicando uma galáxia:
# Se tiver buraco negro supermassivo:
# "Ha um buraco negro supermassivo nesta galaxia, demais! Alem da existencia de cerca de {qnt_planetas} milhoes de planetas"
# Se não tiver:
# "Aparentemente nao ha nenhum buraco negro supermassivo no centro dessa galaxia, jurava que todas tinham! Nao importa, ainda temos {qnt_planetas} milhoes de planetas para observar algum deve apresentar possiblidade de vida"
# Caso seja indicando um buraco negro supermassivo:
# "Conseguimos todas informacoes necessarias para classificar este buraco negro no nosso banco de dados!"
# "De acordo com as analises, o buraco negro:"
# "- Tem massa de aproximadamente {massa} milhoes massas solares"
# "- Possui em media {rotacao} rotacao(oes) por segundo"
# "- {carga}"
# {carga} →
# Caso a carga seja nula:
# "Apresenta carga inexistente ou nula"
# Caso a carga seja positiva:
# "Apresenta carga positiva"
# Caso a carga seja negativa:
# "Apresenta carga negativa"


qtd_instrucoes = 0
while not(1 <= qtd_instrucoes <= 4):
    qtd_instrucoes = input()
    qtd_instrucoes = int(qtd_instrucoes, 2)
for i in range(0, qtd_instrucoes):
    tipo_corpo = input()
    if tipo_corpo == '0101':
        caracteristica_planeta = ''
        beleza = 0
        possivel_vida_extraterra = 0
        agua_aparente = 0
        temp_adequada = 0
        qtd_luas = 0
        while caracteristica_planeta != 'End':
            caracteristica_planeta = input()
            if caracteristica_planeta == 'Beleza':
                beleza = int(input())
            elif caracteristica_planeta == 'Possibilidade de vida extraterrestre':
                possivel_vida_extraterra = int(input())
            elif caracteristica_planeta == 'Agua aparente':
                agua_aparente = int(input())
            elif caracteristica_planeta == 'Temperatura adequada':
                temp_adequada = int(input())
            elif caracteristica_planeta == 'Quantidade de luas':
                qtd_luas = input()
                qtd_luas = int(qtd_luas, 2)
        if agua_aparente == 1 and temp_adequada == 1 and beleza == 1 and possivel_vida_extraterra == 1:
            print(f'Achamos o planeta ideal e ainda tem {qtd_luas} lua(s)!')
            print('Parece bom demais pra ser verdade, que tipo de vida sera que nos aguarda?')
        elif agua_aparente == 1 and temp_adequada == 1 and beleza == 1 and possivel_vida_extraterra == 0:
            print('Ainda nao sabemos se o planeta e habitavel, parece nao haver vida')
        elif agua_aparente == 1 and temp_adequada == 1 and beleza == 0 and possivel_vida_extraterra == 1:
            print(f'O planeta e possivelmente habitavel porem olha essa aparencia, mesmo que tenha {qtd_luas} lua(s) vamos omitir esse do relatorio!')
        else:
            print('Vish! Esse nao satisfaz nem as condicoes basicas, nao perderemos tempo')
    elif tipo_corpo == '1101':
        qtd_planetas_milhoes = ''
        valido = False
        while not valido:
            qtd_planetas_milhoes = input()
            if qtd_planetas_milhoes == '01100100':
                valido = True
            elif qtd_planetas_milhoes == '11001000':
                valido = True
            elif qtd_planetas_milhoes == '100101100':
                valido = True
            else:
                valido = False
        buraco_super = 2
        while buraco_super != 0 and buraco_super != 1:
            buraco_super = int(input())
        if buraco_super == 1:
            print(f'Ha um buraco negro supermassivo nesta galaxia, demais! Alem da existencia de cerca de {int(qtd_planetas_milhoes, 2)} milhoes de planetas')
        else:
            print(f'Aparentemente nao ha nenhum buraco negro supermassivo no centro dessa galaxia, jurava que todas tinham! Nao importa, ainda temos {int(qtd_planetas_milhoes, 2)} milhoes de planetas para observar algum deve apresentar possiblidade de vida')
    elif tipo_corpo == '0000':
        massa = input()
        spin = 2
        while spin != 0 and spin != 1:
            spin = int(input())
        carga = input()
        carga_neutra = False
        carga_negativa = False
        carga_positiva = False
        if carga == '0000':
            carga_neutra = True
        elif carga == '0001':
            carga_positiva = True
        else:
            carga_negativa = True
        print('Conseguimos todas informacoes necessarias para classificar este buraco negro no nosso banco de dados!')
        print('De acordo com as analises, o buraco negro:')
        print(f'- Tem massa de aproximadamente {int(massa, 2)} milhoes massas solares')
        print(f'- Possui em media {spin} rotacao(oes) por segundo')
        if carga_neutra:
            print('- Apresenta carga inexistente ou nula')
        elif carga_positiva:
            print('- Apresenta carga positiva')
        elif carga_negativa:
            print('- Apresenta carga negativa')