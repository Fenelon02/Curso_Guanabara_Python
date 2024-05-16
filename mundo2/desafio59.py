selecionar=0
numero_1=float(input('Digite um valor: '))
numero_2=float(input('Digite um valor: '))

while selecionar!=5:
    soma=print('[ 1 ] somar')

    multiplicar=print('[ 2 ] multiplicar')

    valor_maior=print('[ 3 ] maior')

    trocar_o_numero=print('[ 4 ] novos números')

    parar=print('[ 5 ] sair do programa')

    selecionar=int(input('Escolha a operação desejada: '))

    if selecionar==1:
        adicao=numero_1+numero_2
        print(f' a soma de {numero_1} e {numero_2} é igual a {adicao}')

    elif selecionar==2:
        produto=numero_1*numero_2
        print(f'A multiplicação de {numero_1} e {numero_2} é igual a {produto}')

    elif selecionar==3:
        if numero_1>numero_2:
            print(f'Entre {numero_1} e {numero_2} este é o valor maior {numero_1}')
        else:
            print(f'Entre {numero_2} e {numero_1} este é o valor maior {numero_2}')

    elif selecionar==4:
        numero_1_novo=float(input('Digite o valor novo: '))
        numero_2_novo=float(input('Digite o valor novo: '))

        numero_1=numero_1_novo
        numero_2=numero_2_novo