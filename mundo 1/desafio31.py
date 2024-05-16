distancia=int(input('Digite a distância da sua viagem: '))
if distancia<=200:
    valor=distancia*0.5
    print(f'O valor da sua viagem é R${valor}')
else:
    valor_longe=distancia*0.45
    print(f'O valor para sua viagem é de R${valor_longe}')