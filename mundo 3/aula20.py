#FUNÇÕES

#----PARTE TEÓRICA----

'''
#exemplo de função:


#vai printar '=-' 15 vezes cada vez que eu chamar o 'mostra_linha()'

def mostra_linha():
    print('=-'*15)

mostra_linha()
print('OI')
mostra_linha()





#Para printar algo dentro do que voce deseje

def mensagem(informacao):
    print('-'*30)
    print(f'{informacao}')
    print('-'*30)

mensagem('sistema de alunos')




#Outra forma

def mensagem(informacao):
    print('-'*30)
    print(f'{informacao}')
    print('-'*30)

coisa=input('Digite uma coisa: ')

mensagem(coisa)
'''
#----PARTE PRÁTICA----

'''
def soma(a,b):
    total=a+b
    print(total)

soma(9,7)
soma(8,2)

#pode se alterar a ordem dos parametros
def soma(a,b):
    total=a+b
    print(total)

soma(a=9,b=7)
soma(b=8,a=2)




#outra forma, mais bonito apenas
def soma(a,b):
    print(f'[a]={a} + b={b}')
    total=a+b
    print(f'total igual a {total}')

soma(9,7)
soma(b=8,a=2)

#tem se explicitar um parametro, tem que explicitar todos, nao pode ser como está escrito abaixo
def soma(a,b):
    print(f'[a]={a} + b={b}')
    total=a+b
    print(f'total igual a {total}')

soma(9,7)
'--soma(a=2,4)--'




#o (*x) se usa quando não se sabe quantos paarmetros seão usados,ex:

def contador(*num):
    for item in num:
        print(f'{item} ',end='')
    print(' fim')

contador(1,2,3,4,5,6,7,8)
contador(1,2,3)
contador(1,2,3,4,5)




# só pra frescar
def contador(*num):
    tamanho=len(num)
    print(f'Recebi os valores {num} e são {tamanho} ')
    

contador(1,2,3,4,5,6,7,8)
contador(1,2,3)
contador(1,2,3,4,5)





def dobra(lista):
    posicao=0
    while posicao<len(lista):
        lista[posicao]*=2                                        
        posicao+=1

lista_numeros=[1,2,3,4,5,6]
dobra(lista_numeros)
print(lista_numeros)




def soma(*numeros):
    total=0
    for numero in numeros:
        total+=numero
    print(f'Somando os valores {numeros} se tem o resultado {total}')
soma(1,2,3,4)
'''


