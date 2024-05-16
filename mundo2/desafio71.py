valor_investido=0

continuar=0

while True:

    valor_investido=int(input('Digite o valor a ser sacado: '))
    notas_de_50=valor_investido//50
    valor_investido=valor_investido-notas_de_50*50
    notas_de_20=valor_investido//20
    valor_investido=valor_investido-notas_de_20*20
    notas_de_10=valor_investido//10
    valor_investido=valor_investido-notas_de_10*10
    notas_de_1=valor_investido
    valor_investido=valor_investido*notas_de_1

    print(f'Será sacado {notas_de_50} notas de 50')

    print(f'Será sacado {notas_de_20} notas de 20')

    print(f'Será sacado {notas_de_10} notas de 10')

    print(f'Será sacado {notas_de_1} notas de 1')

    continuar=input('Deseja continuar? [S/N]').upper().strip()[0]

    if continuar=='N':
        break

    if continuar not in 'SN':
        continuar=input('Valor inexistente\nDeseja continuar? [S/N]').upper().strip()[0]

    if continuar=='N':
        break


print('Fim do programa.')
