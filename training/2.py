long_steve=int(input())
lat_steve=int(input())

long_hogs=34 
lat_hogs=220

long_kaka=0
lat_kaka=0

long_soli=140
lat_soli=456

dist_hogs=( (long_steve-long_hogs)**2+(lat_steve-lat_hogs)**2)**0.5
dist_kaka=( (long_steve-long_kaka)**2+(lat_steve-lat_kaka)**2)**0.5
dist_soli=( (long_steve-long_soli)**2+(lat_steve-lat_soli)**2)**0.5

print(f'Distancia para Hogsmeade: {dist_hogs:.2f}')
print(f'Distancia para Kakariko: {dist_kaka:.2f}')
print(f'Distancia para Solitude: {dist_soli:.2f}')