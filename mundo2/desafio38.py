número_1=int(input('Digite um valor: '))
número_2=int(input('Digite um outro valor: '))
número_3=int(input('Digite um terceiro valor: '))



if número_1>número_2 and número_1>número_3:
    print(f'Este é o valor maior {número_1}')

elif número_2>número_1 and número_2>número_3:
    print(f'Este é o valor maior {número_2}')

elif número_1==número_2==número_3:
    print('Não existe valor maior, ambos são iguais')

else:
    print(f'Este é o valor maior {número_3}')
