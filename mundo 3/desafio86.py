'''
Crie um programa que declare uma matriz de dimensão 3×3 
e preencha com valores lidos pelo teclado. 
No final, mostre a matriz na tela, com a formatação correta.
'''
'''
matriz_principal=[[],[],[]]

for contador_1_linha in range(0,3):
    local_0_0=int(input('Digite o número [0,0]: '))
    matriz_principal[0].append(local_0_0)

for contador_2_linha in range(0,3):
    local_1_0=int(input('Digite o número [1,0]: '))
    matriz_principal[1].append(local_1_0)

for contador_3_linha in range(0,3):
    local_2_0=int(input('Digite o número [2,0]: '))
    matriz_principal[2].append(local_2_0)

for montagem_linha_0 in range(0,3):
    print(f'[{matriz_principal[0][montagem_linha_0]}]',end=' ')

print()

for montagem_linha_1 in range(0,3):
    print(f'[{matriz_principal[1][montagem_linha_1]}]',end=' ')

print()

for montagem_linha_2 in range(0,3):
    print(f'[{matriz_principal[2][montagem_linha_2]}]',end=' ')

'''

#minha resolução 2 misturada
matriz_principal=[[0,0,0],[0,0,0],[0,0,0]]

for cada_lista in range(0,3):
    for cada_valor in range(0,3):
        matriz_principal[cada_lista][cada_valor] = int(input(f'Digite um valor para a posição [{cada_lista},{cada_valor}]: '))

for cada_lista in range(0,3):
    for cada_valor_na_lista in range(0,3):
        print(f'[{matriz_principal[cada_lista][cada_valor_na_lista]:^5}]',end=' ')

        #este:^5 faz com que fique 5 espaços centralizados
    print()
