# TRATAMENTO DE ERROS

# ERROS, EXCESSÕES E SEUS TRATAMENTOS

#===PARTE TEÓRICA===

'''
Existem 2 tipos de erros no python:
    -O erro sintático: onde o erro está na frase para programar,exemplo:
        pri--m--t(x)
        # vai aparecer "sintaxerror"
    -E o erro que é excessão  ==exception==, por exemplo, erro de divisão por zero:
        a=int(input('Digite o numerador: '))
        b=int(input('Digite o denominador: '))
            # b não pode ser 0

        resultado=a/b
        print(f'O resultado é {resultado}')
        # se por acaso o b==0 ele vai printar um erro neste b que é zero, e apenas nele, pois a sintaxe está correta, mas 
        # um número não pode ser dividido por zero


Tratamento (resolução) de erros:

    Exemplo:

        try:
            tente fazer alguma coisa
            print(x)

        except:
            somente se a coisa deu errado
            print('deu errado')


        # as estruturas abaixo são opcionais


        else:
            # somente se se o try der certo, 
            print alguma coisa

        finally:
            # Exibido no fim do programa,após o try,except,else 
            faça alguma coisa

'''

# ===PARTE PRÁTICA===

# comando usado
'''
a=int(input('Digite o numerador: '))
b=int(input('Digite o denominador: '))

resultado=(a/b)

print(f'O resultado é {resultado}')



# Uma das formas de fazer
try:
    a=int(input('Digite o numerador: '))
    b=int(input('Digite o denominador: '))

    resultado=(a/b)
            
except:
    print('não deu certo')

else:
    print(f'O resultado é {resultado:.1f}')

finally:
    print('volte sempre')
    

    
# Outra forma de printar erros
try:
    a=int(input('Digite o numerador: '))
    b=int(input('Digite o denominador: '))

    resultado=(a/b)
            
except Exception as erro:
    # este 'Exception' vai mostrar qual foi o erro, o.__class__ vai mostrar de que foi o erro


    print(f'não deu certo, o erro encontrado foi {erro.__class__}')

else:
    print(f'O resultado é {resultado:.1f}')

finally:
    print('volte sempre')
    '''

try:
    a=int(input('Digite o numerador: '))
    b=int(input('Digite o denominador: '))

    resultado=(a/b)
            
except (ValueError,TypeError):
    print('não deu certo, pois você digitou um tipo de daddos diferente.')

except (ZeroDivisionError):
    print('todo número não é divisível por 0')

except KeyboardInterrupt:
    print('O usuário decidiu descontinuar o programa.')

except Exception as erro:
    print(f'não deu certo, o erro encontrado foi {erro.__cause__}')

else:
    print(f'O resultado é {resultado:.1f}')

finally:
    print('volte sempre')
