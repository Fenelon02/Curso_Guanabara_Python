from datetime import date

ano_atual=date.today().year

ano_de_nascimento=int(input('Digite seu ano de nascimento: '))

idade=ano_atual-ano_de_nascimento

if idade<=9:
    print('Categoria mirim.')
elif idade<=14:
    print('Categoria infantil')
elif idade<=20:
    print('Categoria junior')
else:
    print('Categoria master')