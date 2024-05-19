'''
Faça um mini-sistema que utilize o Interactive Help do Python. 
O usuário vai digitar o comando e o manual vai aparecer. 
Quando o usuário digitar a palavra 'FIM', o programa se encerrará. 
--Importante: use cores.--
'''
def listas():
    print('\033[42m=-\033[0m'*30)
    
def funcao_help():
    while True:
        listas()
        funcao_para_ser_exibida=input('\033[42mDigite a fução que deseja mostrar: \033[0m')
        listas()

        print('\033[30m\033[47m')
        print(f'{help(funcao_para_ser_exibida)}\033[0m')
       
        prosseguir=input('\033[37m\033[44m"Deseja prosseguri? ["FIM"] PARA \033[0m').upper().strip()
        # print('\033[0m')
        if prosseguir=='FIM':
            break

funcao_help()
