'''
Aprimore o desafio 93 para que ele funcione com vários jogadores,
 incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
'''

feitos_do_jogador={}
prosseguir='s'
lista_informacoes_dos_jogadores=[]
contador=0
mostrar_dados=1

while prosseguir=='s':

    gols_total=[]

    feitos_do_jogador['nome']=input('Qual nome do jogador? ')
    feitos_do_jogador['partidas']=int(input('Quantas partidas ele jogou? '))

    for item in range(feitos_do_jogador['partidas']):
        gol=int(input(f'na {item+1} partida, quantos gols ele fez? '))

        gols_total.append(gol)
        feitos_do_jogador['gol']=gols_total

        feitos_do_jogador['total']=sum(gols_total)

    lista_informacoes_dos_jogadores.append(feitos_do_jogador.copy())

    prosseguir=input('Deseja prosseguir? [s/n]').lower().strip()[0] 
     
    for pessoa in range(len(lista_informacoes_dos_jogadores)):
        lista_informacoes_dos_jogadores.sort(key=lambda  x:x['total'],reverse=True)



print(f'Código       nome     gols     total')

for item in range(len(lista_informacoes_dos_jogadores)):
    print(f'{item+1:<6}    {lista_informacoes_dos_jogadores[item]['nome']:<4}    {lista_informacoes_dos_jogadores[item]['gol']}    {lista_informacoes_dos_jogadores[item]['total']:>2}')

while True:
    print()
    mostrar_dados=int(input('Deseja mostrar dados de qual jogador? [999]PARA '))

    if mostrar_dados==999:
        print('Volte sempre.')
        break

    if (mostrar_dados)-1>(len(lista_informacoes_dos_jogadores)-1) or mostrar_dados<0:
        mostrar_dados=int(input(f'ERRO! Não há jogadores com o número {mostrar_dados} Deseja mostrar dados de qual jogador? [999]PARA '))

    contador=0

    print(f'Levantamento do jogador {lista_informacoes_dos_jogadores[mostrar_dados-1]['nome']}')

    for item in lista_informacoes_dos_jogadores[mostrar_dados-1]['gol']:
        contador+=1
        print(f'Na partida {contador} ele fez {item} gols')
          