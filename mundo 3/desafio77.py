nomes = ("aurora", 
         "esmeralda", 
         "serpentina", 
         "zephyr", 
         "galateia",
         "nebulosa", 
         "marcelo", 
         "crepúsculo", 
         "aurélia", 
         "azulino")

for palavra_da_vez in nomes:
    print(f'\nNa palavra {palavra_da_vez} temos estas vogais: ',end='')
    for vogal in palavra_da_vez:
        if vogal.lower() in 'aeiou':
            print(vogal,end=' ')