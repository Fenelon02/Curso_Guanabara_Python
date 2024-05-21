'''Vamos ver como fazer acesso a arquivos usando o Python.'''

'''Vamos criar um menu em Python, usando modularização.'''
import modulo_desafio_115
import pacote_de_python.exercicio_115_b.modulo_desafio_115
from time import sleep

arq= 'cursoemvideo.txt'

if not pacote_de_python.exercicio_115_b.modulo_desafio_115.arquivo_existe(arq):

    pacote_de_python.exercicio_115_b.modulo_desafio_115.criar_arquivo(arq)
    
    
while True:
    resposta=modulo_desafio_115.menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa','Sair do programa'])

    if resposta==1:
        # opção de ler o conteúdo de um arquivo
        pacote_de_python.exercicio_115_b.modulo_desafio_115.ler_arquivo(arq)
    elif resposta==2:
        # opção de adcionar uma pessoa
        pacote_de_python.exercicio_115_b.modulo_desafio_115.adcionar_pessoa(arq)
        
    elif resposta==3:
        (modulo_desafio_115.cabecalho('até mais'))
        break
    else:
        print('opção inválida')
    sleep(1)

