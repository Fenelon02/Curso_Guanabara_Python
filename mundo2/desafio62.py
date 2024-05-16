numero=int(input('Digite o 1 termo da progressão aritmética: '))
razao=int(input('Digite a razao  da pa: '))


contador=1
termo=numero
total=0
a_mais=10


while a_mais!=0:
    total+=a_mais

    while contador<=total:
        print(f'{termo} -> ', end='')
        termo+=razao
        contador+=1

    print('esperando..')
    a_mais=int(input('Quantos termos  a mais deseja mostrar?: '))

print(f'Acabou, e foram mostrados {total} termos.')