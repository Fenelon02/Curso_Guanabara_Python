início=int(input('Digite onde quer começar: '))

fim=int(input('Digite onde quer terminar : '))

passo=int(input('Digite qauntos passor quer pular: '))


for c in range (início, fim, passo):
    print(c)

print('Fim')