numero_da_progressao=float(input('Digite um valor e obtenha seus 10 primeiros termos em uma p.a: '))
razao=int(input('Digite a razão de uma p.a: '))
resultado=0

for c in range(1,10):
    resultado=numero_da_progressao+(c-1)*razao
    print(f'Este é o termo {c} que contém este resultado: {resultado}')