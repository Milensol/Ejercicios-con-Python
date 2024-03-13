
i = 1

alumnos = 0

sum_al = 0

mayor_edad = -1

vot_f = 0

while i <= 3:
   
   print('...................................')
   print('        Alumno N° ', i)
   edad = int(input('Ingrese su edad : '))

   sexo = input('Ingrese su sexo : ')

   materia = int(input('Ingrese las materias aprobadas: '))

   if materia >= 4:
      print('Este alumno puede votar')
      alumnos = alumnos + edad
      sum_al = sum_al + 1  

      if sexo == 'f' and edad > 30:
       vot_f = i

      if edad >= mayor_edad:
       mayor_edad = edad       
   else:
     print('Este alumno no puede votar')
      

   i = i + 1
promedio = alumnos / sum_al

print('-----------------------------------------------------------------')
print('-Promedio de edad: ' , promedio)
print(' ')
print('-Cantidad de votantes femeninas mayores de 30 años: ' , vot_f)
print(' ')
print('-Edad mas alta del estudiante que puede votar: ' , mayor_edad)
print('-----------------------------------------------------------------')
