
niños = int(input('Ingrese la cantidad de niños por atender : \n'))
suma_p = 0
me_peso = 99999
ma_peso = -1
for i in range(niños):
   peso = float(input('Ingrese el peso del niño : '))
   suma_p = suma_p + peso
   promedio = suma_p / niños 
   
   if peso >= ma_peso:
        ma_peso = peso
        ord_ma = i

   if peso <= me_peso:
        me_peso = peso
        ord_me = i


print('¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨')
print('Peso Promedio: ' , promedio)
print('¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨')
print('Mayor Peso: ' , ma_peso)
print('Orden Mayor: ' , ord_ma)
print('¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨')
print('Menor Peso: ' , me_peso)
print('Orden Menor: ' , ord_me)
print('¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨')
