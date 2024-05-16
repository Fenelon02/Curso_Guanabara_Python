valor_do_produto=int(input('Digite o valor do produto: '))

a_vista=1
a_vista_cartao=2
parcelado_em_2x_no_cartão=3
parcelado_em_3x_no_cartão=4

metodo_de_pagamento=int(input('Digite 1 para pagamento a vista\n2 para pagamento a vista no cartão\n3para parcelar em até 2x no cartão\n4 paara parcelar em 3x ou mais.'))

if metodo_de_pagamento==1:
    valor_a_vista=valor_do_produto*0.9
    print(f'Este é o valor a vista {valor_a_vista}')
elif metodo_de_pagamento==2: 
    valor_a_vista_no_cartão=valor_do_produto*0.95
    print(f'Este é o valor a vista no cartão {valor_a_vista_no_cartão}')
elif metodo_de_pagamento==3:
    print(f'O valor parcelado em 2x no cartão fica em {valor_do_produto}')
elif metodo_de_pagamento==4:
    valor_parcelado_em_3x_no_cartão=valor_do_produto*1.2
    print(f'O valor parcelado em 3x ou mais no cartão fica em {valor_parcelado_em_3x_no_cartão}')