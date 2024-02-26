
s_basico = float(input('Ingrese el monto de su Sueldo Basico : \n'))

antiguedad = int(input('Ingrese sus años de Antiguedad : \n'))

jubilacion = (11 / 100) * s_basico

o_social = (3 / 100) * s_basico

aporte_s = (2 / 100) * s_basico

adicional = 25 * antiguedad

s_neto = s_basico + adicional - jubilacion - o_social - aporte_s

print('--------------------------------')
print('Sueldo Basico : ' , s_basico)
print(' ')
print('--------DESCUENTOS--------')
print('Jubilacion : ' , jubilacion)
print('Obra Social : ' , o_social)
print('Aportes al Sindicato : ' , aporte_s)
print(' ')
print('--------ADICIONAL--------')
print('Por años de Antiguedad : ', adicional)
print(' ')
print('Sueldo Neto : ', s_neto)
print('--------------------------------')
