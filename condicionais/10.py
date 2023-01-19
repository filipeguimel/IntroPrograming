# Input

# A entrada consiste de seis linhas, contendo os nomes e pontuações finais de cada competidor.
# Nome e pontuação (inteiro) do primeiro amigo:
# nome_1
# pontuação_1
# Nome e pontuação (inteiro) do segundo amigo:
# nome_2
# pontuação_2
# Nome e pontuação (inteiro) do terceiro amigo:
# nome_3
# pontuação_3

# Output

# A saída consiste em três linhas, contendo os pares de nome e pontuação de cada amigo, em ordem do melhor candidato para o pior, com os critérios descritos no enunciado.
# nome e pontuação do primeiro colocado
# nome_primeiro pontuação_primeiro
# nome e pontuação do segundo colocado
# nome_segundo pontuação_segundo
# nome e pontuação do terceiro colocado
# nome_terceiro pontuação_terceiro

nome_1 = input()
pontuacao_1 = int(input())
nome_2 = input()
pontuacao_2 = int(input())
nome_3 = input()
pontuacao_3 = int(input())


if pontuacao_2<pontuacao_1 or (pontuacao_2==pontuacao_1 and nome_2<nome_1):
    nome_2, nome_1 = nome_1, nome_2
    pontuacao_2, pontuacao_1 = pontuacao_1, pontuacao_2

if pontuacao_3<pontuacao_2 or (pontuacao_3==pontuacao_2 and nome_3<nome_2):
    nome_3, nome_2 = nome_2, nome_3
    pontuacao_3, pontuacao_2 = pontuacao_2, pontuacao_3

    if pontuacao_2<pontuacao_1 or (pontuacao_2==pontuacao_1 and nome_2<nome_1):
        nome_2, nome_1 = nome_1, nome_2
        pontuacao_2, pontuacao_1 = pontuacao_1, pontuacao_2

print(f"{nome_1} {pontuacao_1}\n{nome_2} {pontuacao_2}\n{nome_3} {pontuacao_3}")