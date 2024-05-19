'''
Faça um programa que tenha uma função notas() que pode receber várias notas de alunos 
e vai retornar um dicionário com as seguintes informações:

- Quantidade de notas           
- A maior nota                                                                                                                                                                
- A menor nota                                                                                                                                                              – A média da turma                                                                                                                                                      
- A situação (opcional)
'''
def lista_informacoes_de_alunos(*notas,situacao=False):
    """
    ->Função para analisar a média de cada aluno.
    :*notas=guardar as notas de cada aluno, independente da quantidade, por causa do uso do ('*').
    :situacao=(opional) mostrara como está a situação de cada aluno, calssificada em: 
        -Boa para média maior ou igual que 7.
        -Média para média maior ou igual a 5 e menor que 7.
        -Ruim para média menor que 5.
    :return=Vai guardar a variável 'dicionario_geral' que é um dicionário qie armazena todas as informações declaradas.
    
    """
    soma_notas=0

    dicionario_geral={}

    dicionario_geral['total']=len(notas)

    dicionario_geral['maior nota']=max(notas)
    dicionario_geral['menor nota']=min(notas)

    for item in notas:
        soma_notas+=item

    media=dicionario_geral['media']=(soma_notas/dicionario_geral['total'])

    if situacao:

        if dicionario_geral['media']>=7:
            dicionario_geral['situacao']='Boa'
        elif 5<=dicionario_geral['media']<7:
            dicionario_geral['situacao']='Razoável'
        elif dicionario_geral['media']<5:
            dicionario_geral['situacao']='Ruim'

        return dicionario_geral
    
    else:
        return dicionario_geral


mostrar=lista_informacoes_de_alunos(10,10,10,7,situacao=True)
print(f'{mostrar}')
help(lista_informacoes_de_alunos)
