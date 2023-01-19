# Input

# Input O Input será composto por duas entradas:
# A primeira entrada será o nome da música:
# musica - Nome da música
# A segunda entrada, será o gênero da música:
# genero - Gênero da música

# Output

# Caso a música seja aceita:
# ”'nome_da_musica' foi adicionada com sucesso na playlist 'Dandrilha'.”
# Caso não seja aceita:
# ”Ocorreu um erro ao adicionar 'nome_da_musica' na playlist.”

musica=str(input())
genero=str(input())

if genero=='Forró' or genero=='Xote':
  print(f"'{musica}' foi adicionada com sucesso na playlist 'Dandrilha'.")
else:
  print(f"Ocorreu um erro ao adicionar '{musica}' na playlist.")