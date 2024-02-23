import math

x1 = float(input('Ingrese la coordenada del P1 en X : \n'))

y1 = float(input('Ingrese la coordenada del P1 en Y : \n'))

x2 = float(input('Ingrese la coordenada del P2 en X : \n'))

y2 = float(input('Ingrese la coordenada del P2 en Y : \n'))

distancia = (math.sqrt((x2 - x1)**2 + (y2 - y1)**2))

print('Distancia : ' , distancia)


