import math
x=float(input('digite o valor de um angulo'))
y= math.sin(math.radians(x))
c= math.cos(math.radians(x))
h=math.tan(math.radians(x))
print('o angulo escolhido foi de {}, seu seno é {:.2f}, seu cossseno é {:.2f}, e sua tangente é {:.2f}'.format(x,y,c,h))
