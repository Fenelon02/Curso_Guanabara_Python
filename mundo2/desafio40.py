nota_1=int(input('Digite sua primeira nota: '))
nota_2=int(input('Digite sua segunda nota: '))

média=(nota_1+nota_2)/2

if média<5:
    print('Você está reprovado')
elif média>=5 and média<=6.9:
    print('Você está de recuperação.')
elif média>=7:
    print('Você está aprovado')