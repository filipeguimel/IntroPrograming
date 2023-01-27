nome_do_inimigo = input()
inimigos = {'Vingador': 30, 'Tiamat': 20, 'Vingador das Sombras': 14}
if (nome_do_inimigo in inimigos.keys()):
    vida_do_inimigo = inimigos[nome_do_inimigo]
else:
    vida_do_inimigo = 9
turnos = int(input())
armas = {'Chifre': 2, 'Cajado': 4, 'Espada': 6, 'Grande espada': 8, 'Dardo': 12}
armaduras = {'Armadura pesada': 0, 'Armadura media': 1, 'Armadura leve': 3}
personagens = {
    'Bobby': {'arma': 'Grande espada','armor': 'Armadura media'},
    'Diana': {'arma': 'Dardo', 'armor': 'Armadura leve'},
    'Eric': {'arma': 'Grande espada', 'armor': 'Armadura pesada'},
    'Hank': {'arma': 'Espada', 'armor': 'Armadura media'},
    'Presto': {'arma': 'Cajado', 'armor': 'Armadura leve'},
    'Sheila': {'arma': 'Espada', 'armor': 'Armadura leve'},
    'Uni': {'arma': 'Chifre', 'armor': 'Armadura leve'} 
    }
mestre = False
while (turnos > 0 and vida_do_inimigo > 0):
    personagem = input()
    if (personagem == 'Mestre dos Magos'):
        mestre = True
        vida_do_inimigo = 0
    else:
        arma = personagens[personagem]['arma']
        armor = personagens[personagem]['armor']
        turnos -= armaduras[armor] + 1
        vida_do_inimigo -= armas[arma]
else:
    if (mestre):
        print('Muito obrigado amigo, que nos vejamos novamente um dia')
    else:
        if (vida_do_inimigo <= 0):
            print(f'{personagem} executou o ultimo golpe em {nome_do_inimigo}, estamos livres!')
        elif (vida_do_inimigo > 0):
            print(f'Oh nao, {nome_do_inimigo} e muito forte, este e o fim!')