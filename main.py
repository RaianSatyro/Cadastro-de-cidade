from src.classes.cidade import Cidade
import json

sair = False

#abre arquivo jSON
arquivo = open('./src/db/db.json', 'r')
#Lê o arquivo jSON
lista_cidades = json.loads(arquivo.read())
#fecha o arquivo
arquivo.close()


while sair == False:

#Recebendo info da cidade

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
    lista_cidades.append({
        "nome": nova_cidade.nome,
        "populacao": nova_cidade.populacao,
        "uf":{
            "sigla": nova_cidade.uf["sigla"],
            "nome": nova_cidade.uf["nome"],
        }
    })

    resposta = input('Deseja cadastrar outra cidade? (S/N) ')

    #Verificando resposta correta
    resposta_incorreta = resposta.upper() != 'S' and resposta.upper() != 'N'
    while resposta_incorreta:
        print('Resposta deve ser S ou N. ')
        resposta = input('Deseja cadastrar outra cidade? (S/N) ')

    #Finaliza o Cadastro
    if resposta.upper() == 'N':
        sair = True

#Abre o arquivo Json em modo escrita
arquivo = open('./src/db/db.json', 'w')
#Escreve no arquivo json a lista_cidades
arquivo.write(json.dumps(lista_cidades))
#Fecha o arquivo Json
arquivo.close()      