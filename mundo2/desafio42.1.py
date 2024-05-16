lado_1=float(input('Digite um de seus lados: '))
lado_2=float(input('Digite um de seus lados: '))
lado_3=float(input('Digite um de seus lados: '))
if lado_1<lado_2+lado_3 and lado_2<lado_1+lado_3 and lado_3<lado_1+lado_2:
    print('Pode ser um triâmgulo.')
    if lado_1==lado_2==lado_3:
      print('Este é um triângulo equilátero.')
    elif lado_1!=lado_2!=lado_3!=lado_1:
      print('Este é um triângulo escaleno.')
    else:
       print('Este é um triângulo isósceles.')
else:
    print('Não pode ser um triângulo.')
