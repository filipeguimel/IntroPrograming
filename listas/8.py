lista_musicas = []
lista_geral_notas = []
nota_melhor_musica = -1
artista_melhor_musica = ''
nome_melhor_musica = ''
artistas = input()
lista_artistas = artistas.split(' - ')
for artista in lista_artistas:
    musicas = input()
    musicas_artista = musicas.split(' - ')
    lista_musicas.append(musicas_artista)
    nomes_notas_validas = []
    notas_musica = []
    iminencia_voto = 0
    lista_geral_notas.append([])
    for musica in musicas_artista:
        musica_votada = False
        while not musica_votada:
            comentario = input()
            lista_comentario = comentario.split(': ')
            nome_comentario = lista_comentario[0]
            nota_comentario = lista_comentario[1]
            if nota_comentario == '0':
                nota_valida = True
            elif nota_comentario == '1':
                nota_valida = True
            elif nota_comentario == '2':
                nota_valida = True
            elif nota_comentario == '3':
                nota_valida = True
            elif nota_comentario == '4':
                nota_valida = True
            elif nota_comentario == '5':
                nota_valida = True
            elif nota_comentario == '6':
                nota_valida = True
            elif nota_comentario == '7':
                nota_valida = True
            elif nota_comentario == '8':
                nota_valida = True
            elif nota_comentario == '9':
                nota_valida = True
            elif nota_comentario == '10':
                nota_valida = True
            else:
                nota_valida = False
            if nota_valida:
                nome_ja_existia = False
                for nome in nomes_notas_validas:
                    if nome_comentario == nome:
                        notas_musica[0] = int(nota_comentario)
                        nome_ja_existia = True
                if not nome_ja_existia:
                    nomes_notas_validas.append(nome_comentario)
                    notas_musica.append(int(nota_comentario))
                    iminencia_voto += 1
            if iminencia_voto == 2:
                musica_votada = True
                iminencia_voto = 0
                soma_notas_musica = sum(notas_musica)
                lista_geral_notas[lista_artistas.index(artista)].append(soma_notas_musica)
                if soma_notas_musica > nota_melhor_musica:
                    nota_melhor_musica = soma_notas_musica
                    artista_melhor_musica = artista
                    nome_melhor_musica = musica
                nomes_notas_validas = []
                notas_musica = []
escolha_musica = input()
escolha_musica = escolha_musica.split(': ')
musica_escolhida = escolha_musica[1].split(' - ')
artista_musica_escolhida = musica_escolhida[0]
nome_musica_escolhida = musica_escolhida[1]
local_artista_escolhido_em_notas = lista_geral_notas[lista_artistas.index(artista_musica_escolhida)]
local_musica_escolhida_em_musicas = lista_musicas[lista_artistas.index(artista_musica_escolhida)]
nota_musica_escolhida = local_artista_escolhido_em_notas[local_musica_escolhida_em_musicas.index(nome_musica_escolhida)]
diferenca = nota_melhor_musica - nota_musica_escolhida
if diferenca == 0:
    print(f'Caraca {escolha_musica[0]} mandou bem! Essa música é a mais braba, com a nota {nota_musica_escolhida}')
else:
    print(f'Podia ter escolhido outra música, {escolha_musica[0]}. Essa é boa, mas perde em {diferenca} pontos pra a música com a melhor nota')