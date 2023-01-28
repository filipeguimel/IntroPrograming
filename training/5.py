dias=int(input())
casas=int(input())

minutos=(dias*3*60)/2
ticks=minutos*1200

T=ticks/casas

print(int(T))
