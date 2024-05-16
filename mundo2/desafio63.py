tamanho = int(input('Digite quantos números da sequência de Fibonacci deseja: '))

primeiro_termo=0
segundo_termo=1
contador = 0
terceiro_termo_resultado=0

while contador < tamanho: 
   print(f'{terceiro_termo_resultado}', end=', ')


   terceiro_termo_resultado = primeiro_termo + segundo_termo
   primeiro_termo = segundo_termo
   segundo_termo = terceiro_termo_resultado


   contador += 1

print('fim.')


