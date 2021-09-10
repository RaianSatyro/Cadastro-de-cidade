from src.classes.cidade import Cidade
from src.dao.cidadeDAO import cidade_dao_add
from src.dao.cidadeDAO import get_lista_cidade_dao



def cadastrar_cidade():
   
    print('### Cadastrar uma nova cidade ###')

    nome_cidade = input('Digite o nome da cidade: ').title()

    #Verifica se entra é numero inteiro
    populacao_cidade = (input('Digite a população da cidade: '))
    while not populacao_cidade.isnumeric():
        print('Numero inválido')
        populacao_cidade = (input('Digite a população da cidade: '))

    #Trata para que seja digitado apenas letras com 2 caracteres
    sigla_estado = input('Digite a sigla do estado: ').upper()
    while not sigla_estado.isalpha() or len(sigla_estado) > 2:
        print('Sigla inválida')
        sigla_estado = input('Digite a sigla do estado: ').upper()

    nome_estado = input('Digite o nome do estado: ').title()

    #instanciando a cidade
    uf = {'sigla': sigla_estado, 'nome': nome_estado}
    nova_cidade = Cidade(nome_cidade, populacao_cidade, uf)

    #adiciona a cidade na lista
    cidade_dao_add(nova_cidade)


def chama_menu():
    print('''
    ########### Funções ###########
    1 - Listar todas as cidades
    2 - Cadastrar uma nova cidade
    ############### ###############
    0 - Para sair
    ''')

    menu = input('Digite a ação desejada: ')
    if menu == '1':
        for cidade in get_lista_cidade_dao():
            print(f'Nome: {cidade.nome}')
        chama_menu()
        
    elif menu == '2':
        cadastrar_cidade()
        chama_menu()
        
    elif menu =='0':
        print('Saindo...')

    else:
        print('Escolha uma opção valida')
        menu()
