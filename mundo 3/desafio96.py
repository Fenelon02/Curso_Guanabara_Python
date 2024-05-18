'''
Faça um programa que tenha uma função chamada área(), 
que receba as dimensões de um terreno retangular (largura e comprimento) 
e mostre a área do terreno.
'''

def area(largura,coprimento):
    area_total=largura*coprimento
    print(f'A área de um terreno {largura}x{coprimento} é de {area_total}m2')
largura=float(input('Digite a largura do terreno: '))
comprimento=float(input('Digite o comprimento do terreno: '))
area(largura,comprimento)