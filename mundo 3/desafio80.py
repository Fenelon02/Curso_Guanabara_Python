'''
Crie um programa onde o usuário possa digitar cinco valores numéricos 
e cadastre-os em uma lista,
já na posição correta de inserção (sem usar o sort()). 
No final, mostre a lista ordenada na tela.
'''
'''lista=[]
mai=men=meio=0

for c in range(0,5):
    n=(int(input('Digite um número: ')))
    if c==0:
        mai=men=meio=n
    else:
        if n>mai:
            mai=n
        if n<men:
            men=n
        if men<n<mai:
            meio=n
print(lista)'''

lista=[]
for c in range(0,5):
    n=int(input('Digite um valor: '))
    if c==0 or n>lista[-1]:
        lista.append(n)
        print('Adcionado no final da lista')
    else:
        pos=0
        while pos < len(lista):
            if n<=lista[pos]:
                lista.insert(pos,n)
                print(f'Adcionado na posição {pos}')
                break
            pos+=1
print(lista)


