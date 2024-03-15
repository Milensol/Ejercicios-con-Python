
i = 1

s_menor = 99999

t_ina = 0

t_cest = 0

while i <= 3:

 s_bruto = float(input('+Ingrese el importe de su sueldo bruto : $ '))

 ev_desemp = input('+Ingrese el resultado de su evaluacion de desempeño : ')
 
 ina = int(input('+Ingrese las inasistencias que tuvo en el mes : '))
 
 s_neto = s_bruto

 c_est = 0


 if ev_desemp == 'b' and ina == 0:
     c_est = (30/100) * s_bruto
     s_neto = s_bruto + c_est


 if ev_desemp == 'm':
     if s_neto <= s_menor:
         s_menor = s_neto
         empleado = i
 
 
 t_ina = t_ina + ina
 t_cest = t_cest + c_est
 

 print('.......................................')
 print('      Empleado N°' , i)
 print(' ')
 print('Sueldo Bruto : $ ' , s_bruto)
 print(' ')
 print('Por Concepto de Estimulacion : $ ' , c_est )
 print(' ')
 print('Sueldo Neto : $ ' , s_neto)
 print('.......................................')
 
 i = i + 1


print('.......................................')
print('--Menor sueldo de los empleados evaluados con M--')
print('Menor sueldo : $ ' , s_menor )
print('Empleado N° : ' , i)
print('.......................................')
print('-Total de Inasistencias : ' , t_ina)
print(' ')
print('Total a pagar por Concepto de Estimulacion : ' , t_cest)
print('.......................................')
