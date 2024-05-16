from random import randint
from time import sleep

itens=('pedra', 'papel' , 'tesoura')
escolhido_pelo_computador=randint(0, 2)

print('Suas opções: [0] pedra\n[1] papel\n[2] tesoura')
pessoa_jogou=int(input('Digite seu número escolhido: '))

print(f'Jogador jogou {itens[pessoa_jogou]}')
print(f'O escolhido pelo computador foi {itens[escolhido_pelo_computador]}')


#INUTIL APENAS PRA DECORAR
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)

if escolhido_pelo_computador==0:
    if pessoa_jogou==0:
     print('EMPATE')
    elif pessoa_jogou==1:
       print('VENCEU')
    elif pessoa_jogou==2:
       print('PERDEU')
    else:
       print('INVÁLIDO')
    

elif escolhido_pelo_computador==1:
   if pessoa_jogou==0:
      print('PERDEU')
   elif pessoa_jogou==1:
      print('EMPATE')
   elif pessoa_jogou==2:
      print('GANHOU')
   else:
      print('INVÁLIDA')

elif escolhido_pelo_computador==2:
  if pessoa_jogou==0:
     print('GANHOU')
  elif pessoa_jogou==1:
     print('PERDEU')
  elif pessoa_jogou==2:
     print('EMPATE')
  else:
     print('INVÁLIDO')