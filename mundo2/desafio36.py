salario=int(input('Digite seu salário: '))
valor_da_casa=float(input('Digite o valor da casa: '))
anos_de_pagamento=int(input('Digite em quantos anos quer pagar: '))

quantidade_de_meses=anos_de_pagamento*12
valor_mensal=valor_da_casa/quantidade_de_meses

if valor_mensal>salario*0.3:
    print('Sua compra não foi aprovada')
else:
    print('Parabéns! Foi aprovado')
