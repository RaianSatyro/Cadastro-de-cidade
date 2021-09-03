from src.classes.cidade import Cidade
import json

sair = False

#abre arquivo jSON
arquivo = open('./src/bd/bd.json', 'r')
#Lê o arquivo jSON
lista_cidades = json.loads(arquivo.read())
#fecha o arquivo
arquivo.close()

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
arquivo = open('./src/bd/bd.json', 'w')
#Escreve no arquivo json a lista_cidades
arquivo.write(json.dumps(lista_cidades))
#Fecha o arquivo Json
arquivo.close()      