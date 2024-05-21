# SOLUÇÃO GUANABARA
# (a minha eu consegui fazer bem mais ou menos, mas tem muuitos desfalques)

def numero_real(numero):
    while True:
        entrada=input(numero).replace(',','.').strip()

        if entrada.isalpha() or entrada=='':
            print(f'ERRO! "{entrada}" É UM VALOR INVÁLIDO ')

        else:
            return float(entrada)