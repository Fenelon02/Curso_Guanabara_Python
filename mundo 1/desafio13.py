dias=float(input('Digite a quantidade de dias: '))
alugueldias=dias*60
kmrodado=float(input('Digite a quantidade de km rodados: '))
valorkm=kmrodado*0.15
valortotal=valorkm+alugueldias
print(f'O valor total do aluguel dos carros ficou em {valortotal}')