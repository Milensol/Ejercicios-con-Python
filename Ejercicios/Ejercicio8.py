
monto = float(input('Ingrese el monto de su factura de servicio : \n'))

recargo = (12 / 100) * monto

total = monto + recargo

print('*********************************************************')
print('Monto de su factura de servicio : ' , monto)
print(' ')
print('Recargo del 12% por pago fuera de termino : ' , recargo)
print(' ')
print('Total a pagar : ' , total)
print('*********************************************************')
