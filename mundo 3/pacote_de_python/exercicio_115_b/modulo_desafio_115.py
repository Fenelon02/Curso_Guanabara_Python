import modulo_desafio_115

def arquivo_existe(nome):
    try:
        a=open(nome,'rt')
        a.close
    except FileNotFoundError:
        return False
    else:
        return True
    
def criar_arquivo(arq):
    try:
        #este 'wt+' significa write text e o + significa para caso não exista,crie
        criar=open(arq,'wt+')
        criar.close
    except:
        print('Houve um erro na criação do arquivo')
    else:
        print(f'Arquivo {arq} criado com sucesso')

def ler_arquivo(arq):
    try:
        ler=open(arq,'rt')
    except:
        print('ERRO AO LER ARQUIVO')
    else:
        modulo_desafio_115.cabecalho('PESSOAS CADASTRADAS')
        print(ler.read())

def adcionar_pessoa(arq):
    try:
        adcionar=open(arq,'+a')
        nome=input('digite seu nome: ')
        idade=input('digite sua idade: ')
        adcionar.write(f'{nome:<10}{idade:>10}\n')
    except:
        print('ERRO AO ADCIONAR A PESSOA')   
    else:
        print(f'{nome} com {idade} anos de idade adcionado com sucesso')


