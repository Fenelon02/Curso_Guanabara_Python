#MEU CÓDIGO

pares=[]

numero_1=int(input('Digite um número: '))
numero_2=int(input('Digite um número: '))
numero_3=int(input('Digite um número: '))
numero_4=int(input('Digite um número: '))

lista=[numero_1,numero_2,numero_3,numero_4]

tupla=tuple(lista)

print(f'O número 9 aparece {tupla.count(9)} vezes')

if numero_1==3 or numero_2==3 or numero_3==3 or numero_4==3:
   print(f'o numero 3 aparece primeiro em {tupla.index(3)+1} lugar')

else:
   print('O número 3 não foi digitado.')

if numero_1%2==0:
   pares.append(numero_1)

if numero_2%2==0:
   pares.append(numero_2)

if numero_3%2==0:
   pares.append(numero_3)

if numero_4%2==0:
   pares.append(numero_4)

pares=tuple(pares)

print(f'Os números pares são: {pares}')



#CODIGO DO GUANABARA


'''

numero=((int(input('Digite um número: '))), (int(input('Digite um número: '))),
        (int(input('Digite um número: '))),(int(input('Digite um número: '))))

print((f'O número 9 aparece {numero.count(9)} vezes'))

if 3 in numero:
    print(f'o numero 3 aparece primeiro em {numero.index(3)+1} lugar')

else:
   print('O valor 3 é inexistente na tupla.')

print('Os números pares são: ',end='')
for n in numero: 
   if n%2==0:
      print(f' {n}',end='')

'''