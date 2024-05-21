'''Vamos criar um menu em Python, usando modularização.'''
import modulo_desafio_115
from time import sleep
while True:
    resposta=modulo_desafio_115.menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa','Sair do programa'])

    if resposta==1:
        (modulo_desafio_115.cabecalho('opção 1'))
    elif resposta==2:
        (modulo_desafio_115.cabecalho('opção 2'))
    elif resposta==3:
        (modulo_desafio_115.cabecalho('até mais'))
        break
    else:
        print('opção inválida')
    sleep(1)