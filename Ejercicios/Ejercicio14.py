
num1 = int(input('Ingrese su 1er numero entero : \n'))

num2 = int(input('Ingrese su 2do numero entero : \n'))

num3 = int(input('Ingrese su 3er numero entero : \n'))

num4 = int(input('Ingrese su 4to numero entero : \n'))


if num1 > num2 and num1 > num3 and num1 > num4:
    print('Su numero mayor es : ' , num1)
else:
    if num2 > num3 and num2 > num4:
        print('Su numero mayor es : ' , num2)
    else:
        if num3 > num4:
         print('Su numero mayor es : ' , num3) 
        else:
           print('Su numero mayor es : ' , num4) 

