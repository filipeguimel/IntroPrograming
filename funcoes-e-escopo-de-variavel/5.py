
ti= 2*60
gorjetas_totais = 10


def pedras(gorjetas,t):
    tempo = (2*60) - t
    gorjetas = (gorjetas + tempo) / 2
    return int(gorjetas)

def massagem_pes(gorjetas):
    if ((gorjetas%2)==0):
        gorjetas = (gorjetas%7) * 6
    else:
        gorjetas = (gorjetas%7)**2
    return gorjetas


def refeicao(gorjetas):
    if (gorjetas%10)==0:
        gorjetas+=5
    else:
        while((gorjetas%10)!=0):
            gorjetas+=1

    return gorjetas

def massagem_completa(gorjetas):
    m = str(gorjetas)
    for i in m:
        gorjetas += int(i)
    return int(gorjetas)


while (ti>0 and gorjetas_totais < 50):
    serviço = input()
   
    if serviço == "pedras":
        gorjetas_totais += pedras(gorjetas_totais, ti)
        ti-=20
        print(f"Voce concluiu o servico de Pedras Quentes e agora possui {gorjetas_totais} gorjetas.")
        
    elif serviço == "pes":
        gorjetas_totais += massagem_pes(gorjetas_totais)
        ti -= 30
        print(f"Voce concluiu o servico de Massagem nos Pes e agora possui {gorjetas_totais} gorjetas.")
      
    elif serviço == "refeicao":
        gorjetas_totais = refeicao(gorjetas_totais)
        ti -= 15
        print(f"Voce concluiu o servico de Servir Refeicao e agora possui {gorjetas_totais} gorjetas.")
        
    elif serviço == "completa":
        gorjetas_totais = massagem_completa(gorjetas_totais)
        ti -= 50
        print(f"Voce concluiu o servico de Massagem Completa e agora possui {gorjetas_totais} gorjetas.")
    else:
        print(f"O cliente fez voce perder tempo, voce ainda possui {gorjetas_totais} gorjetas.")
        ti -= 5
        
if gorjetas_totais >= 50:
    print(f"Você acumulou {gorjetas_totais} gorjetas, com essa quantidade voce conseguira comprar sua passagem de saida e salvar seus pais.")
elif gorjetas_totais < 50:
    print(f"Voce nao conseguiu o minimo necessario para comprar a passagem de saida desse mundo e salvar seus pais.")