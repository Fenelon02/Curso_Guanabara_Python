def metade(numero=0):
    return f'A metade de {numero} é igual a {numero/2}'

def dobro(numero=0):
    return f'o dobro de {numero} é igual a {numero*2}'

def aumentar(numero=0):
    taxa=int(input('Digite o quanto quer aumentar: '))
    valor_para_aumetar=numero*(taxa/100)
    total_aumentado=numero+valor_para_aumetar
    return f'O valor {numero} acrescido de {taxa}% é igual a {total_aumentado}'

def diminuir(numero):
    taxa=int(input('Digite o quanto quer diminuir: '))
    valor_para_diminuir=numero*(taxa/100)
    total_diminuido=numero-valor_para_diminuir
    return f'o valor {numero} decrescido de {taxa}% é igual a {total_diminuido}'