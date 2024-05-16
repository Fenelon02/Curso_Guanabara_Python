import math
catetooposto=float(input('Digite o valor do cateto oposto: '))
catetoadj=float(input('Digite o valor do cateto adjascente: '))
hipotenusa= math.hypot(catetooposto, catetoadj)
print (f'A hipotenusa vale {hipotenusa:.2f}')