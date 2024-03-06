
nombre = input('Ingrese el nombre del trabajador : \n')

horas = int(input('Ingrese las horas que trabajo : \n'))

tarifa = float(input('Ingrese la tarifa : \n'))

imp = 0

if horas <= 35:
    s_bruto = tarifa * horas
else:
    hs_extra = horas - 35
    s_bruto = (tarifa * 35) + hs_extra * (tarifa * 1.5)



if s_bruto <= 2000:
    s_neto = s_bruto
elif s_bruto >= 2000 and s_bruto <= 2220:
    imp = (20 / 100) * s_bruto
    s_neto = s_bruto - imp
else:
    imp = (30 / 100) * s_bruto
    s_neto = s_bruto - imp


print('...................................')
print('Nombre del Trabajador : ' , nombre)
print(' ')
print('Salario Bruto : $ ' , s_bruto)
print(' ')
print('Impuesto : $ ' , imp)
print(' ')
print('Salario Neto : $ ' , s_neto)
print('...................................')
