'''somar os numeros pares'''

soma=0

for c in range(6):
    numero=int(input('Digite um número: '))

    if numero%2==0:
        soma+=numero
print(f'A soma de todos os números pares é de {soma}')
