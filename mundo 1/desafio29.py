velocidade=int(input('Digite sua velocidade: '))
if velocidade>80:
    print('Você foi multado')
    multa=velocidade-80
    valor_multa=multa*7
    print(f'Sua multa foi no valor de {valor_multa}')
else:
    print('parabèns, você está seguindo a lei')

