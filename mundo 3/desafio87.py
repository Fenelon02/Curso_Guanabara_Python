'''
Aprimore o desafio anterior, mostrando no final:                                                    
A) A soma de todos os valores pares digitados.                                                                                                  
B) A soma dos valores da terceira coluna.                                                                                                                
C) O maior valor da segunda linha.
'''
matriz_principal=[[0,0,0],[0,0,0],[0,0,0]]
total_da_soma_numeros_pares=0
total_da_soma_terceira_coluna=0
maior_valor_segunda_linha=0


for cada_lista in range(0,3):
    for cada_valor in range(0,3):
        matriz_principal[cada_lista][cada_valor] = int(input(f'Digite um valor para a posição [{cada_lista},{cada_valor}]: '))

        if matriz_principal[cada_lista][cada_valor]%2==0:
            total_da_soma_numeros_pares+=matriz_principal[cada_lista][cada_valor]

        if cada_valor==2:
            total_da_soma_terceira_coluna+=matriz_principal[cada_lista][cada_valor]
        
        if cada_lista==1:
            if cada_valor==0:
                maior_valor_segunda_linha=matriz_principal[cada_lista][cada_valor]
            else:
                if maior_valor_segunda_linha<matriz_principal[cada_lista][cada_valor]:
                    maior_valor_segunda_linha=matriz_principal[cada_lista][cada_valor]


for cada_lista in range(0,3):
    for cada_valor_na_lista in range(0,3):
        print(f'[{matriz_principal[cada_lista][cada_valor_na_lista]:^5}]',end=' ')

    print()

print(f'O total da soma dos números pares é {total_da_soma_numeros_pares}')
print(f'O total da soma dos valores da terceira coluna é {total_da_soma_terceira_coluna}')
print(f'O maior valor da segunda linha é o {maior_valor_segunda_linha}')
