import modulo_desafio_108


numero=float(input('Digite um número: '))


# se quiser declarar como euro, é possível, exemplo abaixo:
print(f'o valor {modulo_desafio_108.valor_formatado(numero,'EU$')} aumentando 10% temos {modulo_desafio_108.aumentar(numero,10)}')

print(f'o valor {modulo_desafio_108.valor_formatado(numero)} diminuindo 10% temos {modulo_desafio_108.diminuir(numero,10)}')
print(f'O dobro de {modulo_desafio_108.valor_formatado(numero)} é igual a {modulo_desafio_108.dobro(numero)}')
print(f'O triplo de {modulo_desafio_108.valor_formatado(numero)} é igual a {modulo_desafio_108.metade(numero)}')