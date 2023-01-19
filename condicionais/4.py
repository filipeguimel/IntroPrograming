# Input

# Você receberá na entrada o nome do doce seguido da quantidade vendida, para cada um dos três doces:
# pe de moleque
# quantidade1
# cocada
# quantidade2
# maca do amor
# quantidade3

# Output

# Se Gabi não vender nenhum doce durante a festa, deve ser impressa a mensagem:
# A ideia foi peba! Acho melhor encontrar um novo jeito de ganhar dinheiro...
# Caso contrário, deve-se imprimir:
# Oxe! Você ganhou {faturamento} reais vendendo {melhor_doce}. O povo gostou, visse?!

pe=str(input())
quant_pe=int(input())
cocada=str(input())
quant_cocada=int(input())
maca=str(input())
quant_maca=int(input())

faturamento_pe=quant_pe*2
faturamento_cocada=quant_cocada*5
faturamento_maca=quant_maca*3

if quant_pe==0 and quant_cocada==0 and quant_maca ==0:
  print("A ideia foi peba! Acho melhor encontrar um novo jeito de ganhar dinheiro...")
elif faturamento_pe>faturamento_cocada and faturamento_pe>faturamento_maca:
  print(f'Oxe! Você ganhou {faturamento_pe} reais vendendo {pe}. O povo gostou, visse?!')
elif faturamento_cocada>faturamento_pe and faturamento_cocada>faturamento_maca:
  print(f'Oxe! Você ganhou {faturamento_cocada} reais vendendo {cocada}. O povo gostou, visse?!')
elif faturamento_maca>faturamento_pe and faturamento_maca>faturamento_cocada :
  print(f'Oxe! Você ganhou {faturamento_maca} reais vendendo {maca}. O povo gostou, visse?!')

elif faturamento_pe==faturamento_cocada>faturamento_maca or faturamento_maca==faturamento_cocada>faturamento_pe or faturamento_pe==faturamento_maca>faturamento_cocada:
  if quant_pe>quant_cocada and  quant_pe>quant_maca:
    print(f'Oxe! Você ganhou {faturamento_pe} reais vendendo {pe}. O povo gostou, visse?!')
  elif quant_cocada>quant_pe and quant_cocada>quant_maca:
    print(f'Oxe! Você ganhou {faturamento_cocada} reais vendendo {cocada}. O povo gostou, visse?!')
  elif quant_maca>quant_pe and quant_maca>quant_cocada:
    print(f'Oxe! Você ganhou {faturamento_maca} reais vendendo {maca}. O povo gostou, visse?!')