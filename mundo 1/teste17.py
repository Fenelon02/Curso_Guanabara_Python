import math
x=int(input('digite um número que servirá \n de cateto oposto de um triângulo'))
y=int(input('digite um número que servirá de cateto \n adjascente de um triângulo'))
z= math.hypot(x,y)
print('o resultado da medida da hipotenusa é de {:.2f}'.format(z))