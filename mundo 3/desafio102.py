'''
Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
o primeiro que indique o número a calcular e outro chamado show, 
que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
'''
def fatorial(num=1,show=False):
    """
    ->Função feita para calcular o fatorial de um número
    :Num= Número a ser calculado o fatorial
    :Show= (OPCIONAL)Mostrar ou não o desenrolar do calculo do fatorial
    :Return= retorna o resultado do calculo do fatorial
    """
    print('=-'*num*3)

    resultado=1

    if show==True:
        for contador in range(num,0,-1):
            if contador==1:
                print(' 1 ',end='')
            else:
                print(f' {contador} x',end='')
            
            resultado*=contador
        return f'= {resultado}'
    else:
        for contador in range(num,0,-1):
            resultado*=contador

        return f' {resultado}'

print(fatorial(5,True))
help(fatorial)