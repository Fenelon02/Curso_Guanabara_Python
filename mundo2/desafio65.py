numero=0
contador=0
maior=0
menor=0
total=0
media=0
continuar='s'

while continuar=='s':

    numero=int(input('Digite um número e obtenha sua média: '))
    continuar=input('Deseja continuar? [S/N]\n').lower()[0]
    total+=numero
    contador+=1
    media=total/contador

    if contador==1:
        maior=numero
        menor=numero
        
    if numero>maior:
        maior=numero

    if numero<menor:
        menor=numero

print(f'Esta é a média dos {contador} digitados {media}')
print(f'Este é o valor maior {maior}')
print(f'Este é o valor menor {menor}')
