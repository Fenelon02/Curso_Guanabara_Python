prosseguir='s'
contador_pessoas=0
mais_pesadas=[]
mais_leves=[]
lista_individual=[]
lista_total=[]

while prosseguir=='s':

    lista_individual=[]

    nome=(input('Digite seu nome: '))
    peso=(int(input('Digite seu peso: ')))

    lista_individual.append(nome)
    lista_individual.append(peso)

    lista_total.insert(0,lista_individual[:])
    
    contador_pessoas+=1

    if contador_pessoas == 1:
        mais_leves.append((lista_total[0]))
        mais_pesadas.append((lista_total[0]))


    else:

        if lista_total[0][1]>mais_pesadas[0][1]:
            mais_pesadas.clear()
            mais_pesadas.insert(0,lista_total[0])
            

        elif lista_total[0][1]<mais_leves[0][1]:
            mais_leves.clear()
            mais_leves.insert(0,lista_total[0])
            

        elif lista_total[0][1]==mais_pesadas[0][1]:
            mais_pesadas.insert(0,lista_total[0])

        elif lista_total[0][1]==mais_leves[0][1]:
            mais_leves.insert(0,lista_total[0])



    prosseguir=input('Deseja prosseguir? [S/N]').lower().strip()[0]


print(f'Foram cadastradas {contador_pessoas} ao total.')

print('Nome das pessoas mais leves:')

for pessoa in mais_leves:
    print(f'{pessoa[0]} pesa {pessoa[1]}')

print('Nome das pessoas mais pesadas: ')

for pessoa in mais_pesadas:
    print(f'{pessoa[0]} pesa {pessoa[1]}')

