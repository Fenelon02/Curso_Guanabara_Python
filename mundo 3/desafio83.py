#minha solução
'''
lista=[]
contador_parentese_aberto=0
contador_parentese_fechado=0

while True:

    string = input('digite: ')
    lista = list(string)

    if '(' in lista:
        contador_parentese_aberto=lista.count('(')

        if ')' in lista:
            contador_parentese_fechado=lista.count(')')
           
            if contador_parentese_aberto==contador_parentese_fechado:
                print('expressão correta')

    break 
    '''
#solução do guanabara:
expressao=input('Digite uma expressão: ')
pilha=[]
for simbolo in expressao:
    if simbolo=="(":
        pilha.append('(')
    elif simbolo==")":
        if len(pilha)>0:
            pilha.pop()
        else:
            pilha.append(')')
        break

if len(pilha)==0:
    print('expressão válida.')
else:
    print('expressão inválida.')