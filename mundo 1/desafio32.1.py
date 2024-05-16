from datetime import date
ano=int(input('Digite 0 para receber o ano atual, ou digite qualquer ano: '))
if ano==0:
    ano=date.today().year

if ano%4==0 and ano%100!=0 or ano%400==0:
    print('este ano é bissexto')
else:
    print('este ano não ')
