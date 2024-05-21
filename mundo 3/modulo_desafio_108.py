def metade(numero=0):
    return f'R${numero/2}'

def dobro(numero=0):
    return F'R${numero*2}'

def aumentar(numero,taxa):

    valor_para_aumetar=numero*(taxa/100)
    total_aumentado=numero+valor_para_aumetar
    return f'R${total_aumentado:.2f}'.replace('.',',')

def diminuir(numero,taxa):
    
    valor_para_diminuir=numero*(taxa/100)
    total_diminuido=numero-valor_para_diminuir
    return f'R${total_diminuido:.2f}'.replace('.',',')

def valor_formatado(numero=0,sifrao='R$'):
    return f'{sifrao}{numero:.2f}'.replace('.',',')