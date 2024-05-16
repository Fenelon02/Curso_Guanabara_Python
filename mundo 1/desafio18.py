import math
angulo=float(input('Digite um ângulo: '))
angulonovo= math.radians(angulo)
sen= math.sin(angulonovo)
cos= math.cos(angulonovo)
tg= math.tan(angulonovo)
print (f'O angulo diigtado foi {angulo:.2f}, seu seno é de {sen:.2f}, seu cosseno é de {cos:.2f}, e sua tangente é de {tg:.2f}')