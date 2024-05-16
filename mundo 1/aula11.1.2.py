nome=input('Digite seu nome: ')

cores={ 'amarelo':'\033[34m',
       'azul':'\033[33m',
       'limpa':'\033[m',
       'negrito':'\033[1m]'}

print('Que belo nome,{}{}{}'.format(cores['amarelo'], nome, cores['limpa']))
