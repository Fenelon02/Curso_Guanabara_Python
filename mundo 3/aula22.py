# MÓDULOS E PACOTES

#ACESSAR PASTA 'modulos mundo 3'


#PARTE TEÓRICA
''''''

def fatorial(numero):
    resultado=1
    for contador in range(1,numero+1):
        resultado*=contador
    return resultado

numero=int(input('Digite um número e obtenha seu fatorial: '))
resposta=fatorial(numero)
print(f'O fatorial de {numero} é igual a {resposta}.')


#pacotes

