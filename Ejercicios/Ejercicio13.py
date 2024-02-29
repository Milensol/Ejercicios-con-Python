
sueldo_b = float(input('Ingrese el monto de su sueldo : \n'))

if sueldo_b >= 7000:
    aumento = (12 / 100) * sueldo_b
else:
    if sueldo_b < 7000:
        aumento = (15 /100) * sueldo_b


s_neto = sueldo_b + aumento

print('------------------------------')
print('-------SUELDO BRUTO-------')
print('Sueldo Bruto : ' , sueldo_b)
print(' ')
print('-------ADICIONAL-------')
print('Adicional : ' , aumento)
print(' ')
print('-------SUELDO NETO-------')
print('Sueldo Neto : ' , s_neto)
print('------------------------------')