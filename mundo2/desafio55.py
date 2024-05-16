maior=0
menor=0

for k in range(1,6):
    peso=float(input('digite seu peso: '))

    if k==1:
        maior=peso
        menor=peso

    else:
        if peso>maior:
            maior=peso
        if peso<menor:
            menos=peso

print(f'O maior peso lido foi o de {maior:.2f}kg.')
print(f'O menor peso lido foi de {menor:.2f}kg.')