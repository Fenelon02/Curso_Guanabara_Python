salário=float(input('Digite seu salário: '))
if salário>1250:
    novo_salário=salário*1.10
    print(f'Seu novo salário ficou em R${novo_salário}')
else:
    salário_novo=salário*1.15
    print(f'Seu novo salário ficou em R${salário_novo}')