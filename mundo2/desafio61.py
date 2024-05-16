numero=int(input('Digite o 1 termo da progressão aritmética: '))
razao=int(input('Digite a razao  da pa: '))
contador=1
termo=numero

while contador<=10:
    print(f'{termo} -> ', end='')
    termo+=razao
    contador+=1
print('Fim')