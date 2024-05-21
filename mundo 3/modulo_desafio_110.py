def metade(numero=0,mostrar_moeda=True):

    metade=numero/2
    
    # Outra forma de fazer.
    return metade if mostrar_moeda is False else  valor_formatado(metade)
        
def dobro(numero=0,mostrar_moeda=True):

    dobro=numero*2

    if mostrar_moeda:
        return valor_formatado(dobro)
    else:
        return dobro

def aumentar(numero,taxa,mostrar_moeda=True):

    valor_para_aumetar=numero*(taxa/100)
    total_aumentado=numero+valor_para_aumetar
    if mostrar_moeda:
        return valor_formatado(total_aumentado)
    else:
        return total_aumentado

def diminuir(numero,taxa,mostrar_moeda=True):
    
    valor_para_diminuir=numero*(taxa/100)
    total_diminuido=numero-valor_para_diminuir
    if mostrar_moeda:
        return valor_formatado(total_diminuido)
    else:
        return total_diminuido

def valor_formatado(numero=0,sifrao='R$'):
    return f'{sifrao}{numero:.2f}'.replace('.',',')

def resumo(numero,aumento=0,diminuicao=0):

    print('=-'*21)
    print('Resumo do valor'.center(42))  #center(42) vai centralizar o texto
    print('=-'*21)

    print(f'O valor {numero} com aumento de {aumento}% é igual a {aumentar(numero,aumento)}')
    print(f'O valor {numero} com diminuição de {diminuicao}% é igual a {diminuir(numero,diminuicao)}')
    resposta_metade=f'{metade(numero)}'
    print(f'O dobro de {numero} é igual a {dobro(numero)}')
    print( f'A metade de {numero} é igual a {metade(numero)}')