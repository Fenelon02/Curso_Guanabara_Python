'''
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
'''
lista=[]
valor_inputado=(int(input('Digite um valor: ')))
lista.append(valor_inputado)
prosseguir=input('Deseja prosseguir? [S/N]').strip().lower()[0]

while prosseguir=='s':
    valor_inputado=(int(input('Digite um valor: ')))

    if valor_inputado not in lista:
        lista.append(valor_inputado)
        
    else:
        print('Valor já contido na lista.')
    prosseguir=input('Deseja prosseguir? [S/N]').strip().lower()[0]


print(f'A lista ficou assim: {sorted(lista)}')