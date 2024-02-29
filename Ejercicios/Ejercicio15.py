
ingresos = float(input('Escriba el monto de sus ingresos : \n'))

costo_c = float(input('Ingrese el costo de la casa elegida : \n'))

if ingresos >= 8000:
    adelanto = (15 / 100) * costo_c
    pago_m = (costo_c - adelanto) / 120
    años = 10
else: 
    ingresos < 8000
    adelanto = (30 / 100) * costo_c
    pago_m = (costo_c - adelanto) / 84
    años = 7



print('...............................................')
print('-Monto a pagar por adelantado : $ ' , adelanto)
print(' ')
print('-Monto a pagar por mes : $ ' , pago_m)
print(' ')
print('-Cantidad de años a pagar : ' , años)
print('...............................................')
    
    