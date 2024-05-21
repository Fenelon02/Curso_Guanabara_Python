# SOLUÇÃO GUANABARA
# (a minha eu consegui fazer bem mais ou menos, mas tem muuitos desfalques)

def numero_real(numero):
    valido=False
    while not valido:
        entrada=input(numero).replace(',','.').strip()

        if entrada.isalpha() or entrada=='':
            print(f'ERRO! "{entrada}" É UM VALOR INVÁLIDO ')

        else:
            valido=True
            return float(entrada)