from src.classes.cidade import Cidade

sair = False

lista_cidades = []

while sair == False:

    #Recebendo info da cidade
    nome_cidade = input('Digite o nome da cidade: ')
    populacao_cidade = int(input('Digite a população da cidade: '))
    sigla_estado = input('Digite a sigla do estado: ')
    nome_estado = input('Digite o nome do estado: ')

    #instanciando a cidade
    uf = {'sigla': sigla_estado, 'nome': nome_estado}
    nova_cidade = Cidade(nome_cidade, populacao_cidade, uf)

    #adiciona a cidade na lista
    lista_cidades.append(nova_cidade)

    resposta = input('Deseja cadastrar outra cidade? (S/N) ')

    #Verificando resposta correta
    resposta_incorreta = resposta.upper() != 'S' and resposta.upper() != 'N'
    while resposta_incorreta:
        print('Resposta deve ser S ou N. ')
        resposta = input('Deseja cadastrar outra cidade? (S/N) ')

    #Finaliza o Cadastro
    if resposta.upper() == 'N':
        sair = True

print(lista_cidades)        