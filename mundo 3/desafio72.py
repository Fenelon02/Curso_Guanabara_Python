numeros=('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
          'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

escolha=int(input('Digite o número desejado, obtenha sua forma escrita por extenso: '))

while escolha<0 or escolha>20:
    escolha=int(input('Valor inexistente. Digite o número desejado, obtenha sua forma escrita por extenso: '))
    
print(f'Você escolheu o número {numeros[escolha]}')