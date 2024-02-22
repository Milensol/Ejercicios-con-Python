
x1 = int(input('Ingrese la coordenada del P1 en X : \n'))

y1 = int(input('Ingrese la coordenada del P1 en Y : \n'))

x2 = int(input('Ingrese la coordenada del P2 en X : \n'))

y2 = int(input('Ingrese la coordenada del P2 en Y : \n'))

import math

distancia = (math.sqrt((x2 - x1)**2 + (y2 - y1)**2))

print('Distancia : ' , distancia)


