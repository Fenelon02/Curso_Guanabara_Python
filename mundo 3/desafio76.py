valores_e_produtos = ('LÁPIS', 1.00, 
                    'BORRACHA', 2.50,
                    'CANETA', 2.00,
                    'CADERNO', 5.00,
                    'RÉGUA', 1.50,
                    'TESOURA', 3.00,
                    'APONTADOR', 1.20,
                    'MARCA-TEXTO', 1.80,
                    'GRAMPO', 0.50,
                    'COLA', 2.30)

for posiçaõ in range(0,len(valores_e_produtos)):
    if posiçaõ%2==0:
        print(f'{valores_e_produtos[posiçaõ]:.<30}',end='')
    else:
        print(f'R${valores_e_produtos[posiçaõ]:.2f}')
    