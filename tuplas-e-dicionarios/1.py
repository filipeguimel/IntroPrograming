# Input

# Ao receber o comando ‘ADD’ também virá o nome do Pokémon que deve ser adicionado, e depois, mais um input com a descrição do Pokémon.
# Ex.:
# ADD Charmander
# Tem preferência por coisas quentes. Quando chove, diz-se que o vapor jorra da ponta de sua cauda.
# Ao receber o comando ‘DESC’, também virá em seguida o nome do Pokémon que que ele quer a descrição:
# Ex.:
# DESC Charmander
# Dica: Use try/except com EOFError para pegar as entradas.

# Output

# Ao receber o comando ‘ADD’, caso o Pokémon, já tenha sido adicionado, a Pokédex deverá printar, ‘Pokémon já adicionado na Pokédex’.
# Caso o Pokémon não tenha sido adicionado ainda, a Pokédex tem que adicionar, e printar, ‘Pokémon adicionado com sucesso’
# Ao receber o comando ‘DESC’, caso o pokémon não tenha sido adicionado ainda, a Pokédex deve printar, ‘Ainda não há registro desse Pokémon’.
# Caso o Pokémon já tenha sido adicionado, ela deve printar a descrição do Pokémon escolhido.

algoritmo = True
pokedex = {}
while (algoritmo):
    try:
        comando, nome = input().split(" ")
        
        if (comando == "ADD"):
            if (nome in pokedex.keys()):
                print("Pokémon já adicionado na Pokédex")
            else:
                description = input()
                pokedex[nome] = description
                print("Pokémon adicionado com sucesso")
        elif (comando == "DESC"):
            if (nome not in pokedex.keys()):
                print("Ainda não há registro desse Pokémon")
            else:
                print(pokedex[nome])
    except EOFError:
        algoritmo = False