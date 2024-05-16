numero=0
contador=0
total=0

while numero!=999:

    numero=int(input('Digite números e obenha a soma entre eles.\n[999] para a soma\n'))

    if numero!=999:
        total+=numero
        contador+=1

print(f'A soma dos {contador} algarismos deu um total de {total}.')
    
    