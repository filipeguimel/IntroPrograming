ingredientes = {
    'trigo': {'estoque': 5, 'preco': 3},

    'fermento': {'estoque': 5, 'preco': 2},

    'manteiga': {'estoque': 5, 'preco': 6},

    'batata': {'estoque': 5, 'preco': 4},

    'arroz': {'estoque': 5, 'preco': 3},

    'siri': {'estoque': 5, 'preco': 8},

    'pao': {'estoque': 5, 'preco': 2},

    'tomate': {'estoque': 5, 'preco': 2},

    'alface': {'estoque': 5, 'preco': 1},

    'picles': {'estoque': 5, 'preco': 3},

    'queijo': {'estoque': 5, 'preco': 5},

    'ovos': {'estoque': 5, 'preco': 2}
}
receitas = { 
    'hamburguer de siri': { 'recipe': ('siri', 'pao', 'alface', 'tomate', 'queijo', 'picles'), 'preco': 24},
    'pizza de siri': { 'recipe': ('siri', 'trigo', 'fermento', 'ovos', 'queijo'), 'preco': 42 },
    'siri frito': { 'recipe': ('siri', 'manteiga'), 'preco': 15 },
    'siri a parmegiana': { 'recipe': ('siri', 'trigo', 'ovos', 'queijo', 'tomate'), 'preco': 24 }
}
controle_de_pedidos = {'hamburguer de siri': 0, 'pizza de siri': 0, 'siri frito': 0, 'siri a parmegiana': 0}
caixa = 40
aberto = True
while (aberto):
    try:
        pedido = input()
        if (pedido in (receitas.keys())):
            controle_de_pedidos[pedido] += 1
            
            for ingrediente in receitas[pedido]['recipe']: # Atualiza estoque e compra mais quando precisa
                if (ingredientes[ingrediente]['estoque'] > 0):
                    ingredientes[ingrediente]['estoque'] -= 1
                else:
                    ingredientes[ingrediente]['estoque'] += 3
                    caixa -= (ingredientes[ingrediente]['preco']) * 4
            caixa += receitas[pedido]['preco']
            controle_de_pedidos[pedido] += 1
            print(f'{pedido} saindo...')
        elif (pedido in (controle_de_pedidos.keys())):
            controle_de_pedidos[pedido] += 1
            if (controle_de_pedidos[pedido] > 2):
                controle_de_pedidos[pedido] -= 2
                novo_pedido = input().split(" ")
                receitas[pedido] = {'recipe': (), 'preco': 5}
                receitas[pedido]['recipe'] = tuple(novo_pedido)
                for ingrediente in receitas[pedido]['recipe']: # novo preço da receita
                    receitas[pedido]['preco'] += ingredientes[ingrediente]['preco']
                print(f'Atendendo demandas, {pedido} é a mais nova adição ao cardápio do Siri Cascudo.')
            else:
                print(f'{pedido} ainda não é uma opção disponível.')
        else:
            controle_de_pedidos[pedido] = 1
            print(f'{pedido} ainda não é uma opção disponível.')
    except EOFError:
        aberto = False
        print("##### Fim do expediente #####")
        print(f'O lucro obtido no dia de hoje foi de R${caixa - 40}.')
        mais_pedido = max(controle_de_pedidos.values())
        for key in (controle_de_pedidos.keys()):
            if (controle_de_pedidos[key] == mais_pedido):
                nome_do_mais_pedido = key
        if (nome_do_mais_pedido == 'hamburguer de siri'):
            print('O bom e tradicional hambúrguer de siri, líder em vendas, nunca será superado!')
        else:
            print(f'{nome_do_mais_pedido.capitalize()} está fazendo sucesso entre os clientes, ultrapassando até mesmo o lendário hambúrguer de siri.')