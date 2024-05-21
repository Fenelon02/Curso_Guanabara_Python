from desafio113 import leitor_de_numeros_inteiros

def titulo(tam=42):
    return '='*tam

def cabecalho(nome):
    print(titulo())
    print(nome.center(42))
    print(titulo())

def menu(lista):
    from desafio113 import leitor_de_numeros_inteiros
    cabecalho('lista de informações')
    contador=1
    for item in lista:
        print(f'{contador} - {item}')
        contador+=1
    print(titulo())
    opcao=leitor_de_numeros_inteiros('Sua opção: ')
    return opcao