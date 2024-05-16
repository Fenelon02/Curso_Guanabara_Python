import random
aluno1=input('Qual seu nome? ')
aluno2=input('Qual seu nome? ')
aluno3=input('Qual seu nome? ')
aluno4=input('Qual seu nome? ')
lista=[aluno1,aluno2, aluno3, aluno4]
random.shuffle(lista)
print('a lista fica.')
print(lista)