import random
a=str(input('aluno um: '))
b=str(input('aluno dois: '))
c=str(input('aluno três: '))
d=str(input('aluno quatro: '))
lista=[a,b,c,d]
x=random.choice(lista)
print('o aluno escolhido foi {}'.format(x))