contador_preco=0

total=0

produto_mais_de_1000=0

mais_barato=0

contador_mais_barato=0

while True:
    produto=input('Digite o nome do produto: ')
    preco=float(input(f'Digite o valor do {produto}: '))
    
    if preco>=0:
        total+=preco
        contador_preco+=1

    if preco>1000:
        produto_mais_de_1000+=1

    if contador_preco==1:
        mais_barato=produto
        contador_mais_barato=preco
    
    if  contador_preco!=1 and contador_mais_barato>preco:
        mais_barato=produto
        contador_mais_barato=preco

    prosseguir=input('Deseja prosseguir? [S/N] ').upper().strip()[0]
    if prosseguir in 'Nn':
            break

    while prosseguir not in 'SN':
        prosseguir=input('Digite S/N\nDeseja prosseguir? [S/N] ').upper().strip()[0]

    if prosseguir=='N':
        break

print(f'O total gasto na compra foi de R${total:.2f}')

print(f'Foram comprados {produto_mais_de_1000} produtos com valor acima de R$1000,00')

print(f'O produto mais barato foi o {mais_barato}, que custou R${contador_mais_barato:.2f}')
