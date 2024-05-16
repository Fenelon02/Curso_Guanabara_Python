dia=int(input('Digite uma data do mês: '))

if dia==12:
    print('Acertou!')
elif dia in [21, 22, 23, 24, 25, 26]:
    print('Foi quase o dobro, ou um pouco mais ou menos que isso!')
elif dia==11 or dia==13:
    print('Quase lá, chegou perto!')
else:
    print('Errou feio!')