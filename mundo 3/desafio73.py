times = ('Atlético Mineiro', 'Palmeiras', 'Fortaleza', 'Bragantino', 'Flamengo', 'Athletico Paranaense', 'Ceará', 'Santos', 'Atlético Goianiense',
          'Bahia', 'Fluminense', 'Corinthians', 'Juventude', 'Internacional', 'América Mineiro', 'São Paulo', 'Cuiabá', 'Sport Recife',
            'Grêmio', 'Chapecoense')

print(f'Os 5 primeiros colocados são:{times[0:5]}')

print(f'Os 4 últimos colocados são:{times[-4:]}')

print(f'Os times em ordem alfabética:\n{sorted(times)}')

print(f'A chapecoense está na posição {times.index('Chapecoense')+1}')
