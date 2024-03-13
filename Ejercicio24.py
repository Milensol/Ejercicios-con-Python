
cantidad_l = 0

cantidad_lf = 0

cantidad_lc = 0

me_cantidad = 9999

ma_cantidad = -1

for i in range(1,4):
 print('°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°')
 alimento = input('-Ingrese el alimento que consumio la vaca : ')

 clima = int(input('-Ingrese el clima en el que fue criada : '))

 lit_leche = float(input('-Ingrese los litros de leche que produjo : '))
 
 if alimento == 'f':
     cantidad_lf = lit_leche + cantidad_lf

 if alimento == 'c':
     cantidad_lc = lit_leche + cantidad_lc

 if clima == 2:
     if lit_leche <= me_cantidad:
         me_cantidad = lit_leche 
     if lit_leche >= ma_cantidad:
         ma_cantidad = lit_leche  
     


print('-----------------------------------------------------------')
print(' ')
print('Cantidad de leche de vacas que consumieron el alimento F : ' , cantidad_lf)
print(' ')
print('Cantidad de leche de vacas que consumieron el alimento C : ' , cantidad_lc)
print(' ')
print('Menor cantidad de lts de leche en clima fresco : ' , me_cantidad)
print(' ')
print('Mayor cantidad de lts de leche en clima fresco : ' , ma_cantidad)
print(' ')
print('Alimento con el que produjeron mas lts de leche : ' , alimento)
print('-----------------------------------------------------------')

















