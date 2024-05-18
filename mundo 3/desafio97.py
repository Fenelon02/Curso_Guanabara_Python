'''
Faça um programa que tenha uma função chamada escreva(),
que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.                                  
Ex:                                                                                                                  
escreva('Olá, Mundo!') Saída:                                                                                                                          
~~~~~~~~~  
Olá, Mundo!        
~~~~~~~~~         
'''

def texto(mensagem):
    print('~'*((len(mensagem))+4))
    print(f'  {mensagem}')
    print('~'*((len(mensagem))+4))

texto('oi')
texto('gustavo guanabara')