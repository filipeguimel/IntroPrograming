def meses_pra_anos(meses_totais):
    if meses_totais < 12:
        return 0
    else:
        return meses_pra_anos(meses_totais - 12) + 1

qt_acontecimentos = int(input())

nivel = input().split(', ')

datas = input().split(', ')
meses = []
for data in datas:
    data_separada = data.split('.')
    meses.append((int(data_separada[1])*12 + int(data_separada[0])))

acontecimentos = input().split(', ')

data_atual = input().split('.')
meses_atuais = (int(data_atual[1])*12) + int(data_atual[0])

baixa = 0
media = 0
alta = 0

intervalo = []

for r in nivel:
    mes = meses[0]
    intervalo.append(meses_atuais - mes)
    if meses_atuais - mes > 54:
        alta += 1
    elif int(r) <= 4:
        baixa += 1
    elif int(r) <= 6:
        media += 1
    else:
        alta += 1
    meses.pop(0)

if baixa + media > 0:
    inseguranca = int((media/(baixa + media))*100)

if alta > 0:
    print('Realizar essa operação é um grande erro. A humanidade pode entrar em colapso.')
    print(f'Há {alta} acontecimento(s) relevante(s). Se as consequências das suas ações anularem algum desses eventos, teremos sérios problemas.')
elif inseguranca > 20:
    print('Os cálculos mostram que é possível acessar essa linha do tempo sem que haja muitos danos.')
    print(f'Mas é necessário termos cuidado, a taxa de insegurança é de {inseguranca:}%')
else:
        print('Os cálculos mostram que é possível acessar essa linha do tempo sem que haja muitos danos.\nA chance de sucesso é muito alta. Mudaremos o mundo mais uma vez, dr. Helena Smith.')

print('\nAqui estão os dados dos acontecimentos:')

for quantidade in range(qt_acontecimentos):
    total_anos = int(intervalo[quantidade])
    meses_restantes = (int(intervalo[quantidade]) % 12)
    print(f"{acontecimentos[quantidade]} | gap: {meses_pra_anos(total_anos)} anos e {meses_restantes} meses | nível de relevância: {nivel[quantidade]}")