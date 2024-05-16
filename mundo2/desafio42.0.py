lado_1=float(input('Digite um de seus lados: '))
lado_2=float(input('Digite um de seus lados: '))
lado_3=float(input('Digite um de seus lados: '))
if lado_1<lado_2+lado_3 and lado_2<lado_1+lado_3 and lado_3<lado_1+lado_2:
    print('Pode ser um triâmgulo.')
    equilátero=lado_1==lado_2==lado_3
    print(f'Este é um triângulo equilátero? {equilátero}.')
    isósceles=lado_1==lado_2 or lado_2==lado_3
    print(f'este é um triangulo isósceles? {isósceles}.')
    escaleno=lado_1!=lado_2!=lado_3
    print(f'este é um triângulo escaleno? {escaleno}')
else:
    print('Não pode ser um triângulo.')
