frase=input('Digite uma frase e veja se ela é um paíndromo: ').lower()

palavra= frase.split()
junto=''.join(palavra)

inverso=''

for i in range(len(junto)-1,-1,-1):
    inverso+=junto[i]
if inverso==junto:
    print(f'A frase: {frase}\nÉ um palídromo.')
else:
    print(f'a frase: {frase} \nNão é um palíndromo')

