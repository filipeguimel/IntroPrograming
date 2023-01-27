talismas = {
    "Carneiro" : {"habilidade": "Adormecer", "requisito": "Imortalidade", "talisma_necessario" : "Cao"}, 

    "Cao": {"habilidade": "Imortalidade", "requisito": "Forca descomunal", "talisma_necessario" : "Touro"},

    "Cobra": {"habilidade": "Invisibilidade", "requisito": "Equilibrio espiritual", "talisma_necessario" : "Tigre"},

    "Coelho" : {"habilidade": "Alta velocidade", "requisito": "Metamorfose animal", "talisma_necessario" : "Macaco"},

    "Tigre" : {"habilidade": "Equilibrio espiritual", "requisito": "Adormecer", "talisma_necessario" : "Carneiro"}, 

    "Dragao" : {"habilidade": "Fogo", "requisito": "Cura", "talisma_necessario" : "Cavalo"},

    "Cavalo": {"habilidade": "Cura", "requisito": "Levitacao", "talisma_necessario" : "Galo"}, 

    "Macaco": {"habilidade": "Metamorfose animal", "requisito": "Raio laser", "talisma_necessario" : "Porco"},

    "Galo": {"habilidade": "Levitacao", "requisito": "Animar objetos", "talisma_necessario" : "Rato"}, 

    "Porco": {"habilidade": "Raio laser", "requisito": "Fogo", "talisma_necessario" : "Dragao"},

    "Rato": {"habilidade": "Animar objetos", "requisito": "Alta velocidade", "talisma_necessario" : "Coelho"}, 

    "Touro": {"habilidade": "Forca descomunal", "requisito": "Invisibilidade", "talisma_necessario" : "Cobra"}
    }
talismas_do_jackie = int(input())
habilidades = []
for i in range (talismas_do_jackie):
    talisma = input()
    habilidades.append(talismas[talisma]["habilidade"])
adversarios = int(input())
adversarios_derrotados = 0
for i in range (adversarios):
    talismas_dos_adversarios = input()
    if (talismas[talismas_dos_adversarios]["requisito"] in habilidades):
        habilidades.append(talismas[talismas_dos_adversarios]["habilidade"])
        print(f"Boa! O talisma do {talismas_dos_adversarios} vai ser nosso!")
        adversarios_derrotados += 1
    else:
        requisito = (talismas[talismas_dos_adversarios]["talisma_necessario"])
        print(f"Nao vai dar, melhor ir atras do talisma do {requisito} antes.")
if (adversarios_derrotados == adversarios):
    print("Esse plano funciona, vamos agora!")
else:
    print("Que mau dia!! Melhor pensarmos num plano de fuga.")