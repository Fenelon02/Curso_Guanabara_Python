# FUNÇÕES PARTE 2

# ---PARTE TEÓRICA---

'''
--Interactive help---

==help()==

-Como acessar:
Abra o VS Code.
Abra ou crie um arquivo Python.
Abra o terminal integrado (View > Terminal ou Ctrl + ).
Digite python no terminal e pressione Enter para iniciar o console Python.
Digite 'help()'
digite o que vc quer saber

-Como sair
digite 'quit'

outra forma:
help(print)
-vai mostrar as funcionalidades e 'usuabilidades adcionais' do print, tipo um manual.

outra forma:
print(input.__doc__)



---docstring---
-Um documento de sua função criada
ex: 
def contador(inicio,fim,passos):

    ###esta é sua docsrting###

    para criar é só por 3 aspas duplas abaixo da 1 linha do comando def

    """
    ->Faz uma contagem e mostra na tela
    :Inicio=Número que começa
    :Fim=número que termina
    :Passo=quantos  passos ele pula
    :Return=0,sem retorno
    """

    contador_numerico=inicio

    while contador_numerico<=fim:

        print(f' {contador_numerico}',end='')
        contador_numerico+=passos

    print(' fim')

contador(0,100,10)

help(contador)



---parametros opcionais---

-cria valores padrões para os objetos, tornando sua presença opcionais.

def somar(a=0,b=0,c=0):
    total=a+b+c
    print(f'A soma destes valores é {total}.')

somar(2,9,3)
somar(1,7)
somar()




---escopo de variável---

==existem 2 tipos de variável, a local e a global:
    local=só funciona dentro da função, usável apenas nela
    global=funciona dentro  e fora da função

Para visualizar melhor execute este código abaixo:

def teste(b):
    a=8
    # -este a é o a local, só vale aqui
    b+=4
    c=2
    print(f'dentro de teste a variável a vale {a}')
    print(f'dentro de teste a variável b vale {b}')
    print(f'dentro de teste a variável c vale {c}')
a=5
teste(a)
print(f'A variável A fora de teste vale: {a}')


==para transformar uma vaiável A local numa variável A glogbal

def teste(b):
    global a
    a=8
    # -este a se transforma na naviável a global,ou seja, vai ser o mesmo para dentro e para fora
    b+=4
    c=2
    print(f'dentro de teste a variável a vale {a}')
    print(f'dentro de teste a variável b vale {b}')
    print(f'dentro de teste a variável c vale {c}')



a=5
# este a =5 vira a=8 por conta que foi transformado numa variável global. 
teste(a)
print(f'A variável A fora de teste vale: {a}')


---return---

==return x==

-return serve para guardar uma variável e armazenar em alguma coisa, exemplo:

def somar(a=0,b=0,c=0):
    total=a+b+c
    return total

resposta_1=somar(2,9,3)
resposta_2=somar(1,7)
resposta_3=somar(3)
print(f'O resultado das somas é {resposta_1},{resposta_2},{resposta_3}.')
'''

# PARTE PRÁTICA
'''
==descobrir fatorial de um número
def fatorial(num=1):

    resultado=1

    for contador in range(num,0,-1):
        resultado*=contador

    return resultado

numero=int(input('Digite um número: '))
print(f'O fatorial do número {numero} é igul a {fatorial(numero)}')


def par(numero=0):
    if numero%2==0:
        return True
    else:
        return False
numero=int(input('Digite um número: '))

if par(numero):
    print(f'{numero} é par')
else:
    print(f'{numero} é impar')
'''