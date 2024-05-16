gender=input('Digite seu sexo. [M/F]: ').strip().upper()[0]


'''o [0] so pega a 1 letra'''


while gender not in 'MmFf':
    sexo=input('Errado, digite novamente: ').strip().upper()[0]
print(f'{gender}')