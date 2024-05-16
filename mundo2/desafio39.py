from datetime import date

ano=date.today().year

ano_de_nascimento=int(input('Digite seu ano de nascimento: '))

idade=ano-ano_de_nascimento

if idade==18:
    print('Está na hora de se alistar.')
elif idade<18:
    tempo_que_falta=18-idade
    print(f'Ainda não é hora de se alistar, faltam {tempo_que_falta} anos.')
else:
    tempo_que_passou=idade-18
    print(f'Já passou da hora de se alistar, já se passaram {tempo_que_passou} anos.')