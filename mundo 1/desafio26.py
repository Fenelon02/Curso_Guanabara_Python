letraa=str(input('Digite uma frase e observe quantas vezes\n a letra A ocorre,\n onde aparece primeiro\n e onde aparece por ultimo: ')).lower()
letraa=letraa.strip()
semespaco= letraa.count('a')  
print(f'a letra A aparece {semespaco} vezes')
primeiravez=letraa.find('a')+1
print(f'A letra A aparece pela primeira vez na posição {primeiravez}')
print('A letra a aparece pela ultima vez ena posição {}'.format(letraa.rfind('a')))

