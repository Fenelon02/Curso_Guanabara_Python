tabuada=0
numero=0
total=0


while True:
    numero=int(input('Digite um valor positivo, e obtenha sua tabuada. \nDigite qualquer número negativo para parar.\n'))

    if numero<0:
            print('Acabou')
            break

    for c in range(0,10+1):
        total=c*numero
        print(f'{c} *   {numero}={total}')
