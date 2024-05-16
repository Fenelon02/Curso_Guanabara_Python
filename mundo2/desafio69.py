'''Crie um programa que leia a idade e o sexo de várias pessoas. 
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. 
No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.'''


contador_mulheres=0
contador_idade_mulheres=0

contador_homens=0
contador_idade_homens=0

genero=0

idade=0
contador_idade_geral=0

while True:
    idade=int(input('Qual sua idade? '))
    genero=input('Qual seu gênero? [M/F]').upper().strip()[0]

    if idade>18:
        contador_idade_geral+=1

    if genero in 'Mn':
        contador_homens+=1
        

    if idade<20:
        if genero in 'Ff':
            contador_idade_mulheres+=1
    
    continuar=input('Deseja continuar? [S/N]').upper().strip()[0]


    if continuar in 'Nn':
        break


print(f'Existem {contador_idade_geral} pessoas com idade superior a 18 anos\nForam cadastrados {contador_homens} homens\nExistem  {contador_idade_mulheres} mulher com idade menor  que 20 anos')   