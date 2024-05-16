contador=1
numero=0
soma=0
contador=0

while True:
    numero=int(input('Digite um número: \nDigite [999] para parar o programa'))
    if numero==999:
        break
    soma+=numero
    contador+=1
    
print(f'A soma dos {contador} números é de {soma}')