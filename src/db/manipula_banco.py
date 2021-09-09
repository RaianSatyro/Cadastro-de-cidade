import json

def get_list_cidades():
    #abre arquivo jSON
    arquivo = open('./src/db/db.json', 'r')
    #Lê o arquivo jSON
    lista_cidades = json.loads(arquivo.read())
    #fecha o arquivo
    arquivo.close()
    return lista_cidades


def set_list_cidades(lista_cidades):
    #Abre o arquivo Json em modo escrita
    arquivo = open('./src/db/db.json', 'w')
    #Escreve no arquivo json a lista_cidades
    arquivo.write(json.dumps(lista_cidades))
    #Fecha o arquivo Json
    arquivo.close() 


def add_cidade(nova_cidade):
    cidade_json = {
        "nome": nova_cidade.nome,
        "populacao": nova_cidade.populacao,
        "uf":{
            "sigla": nova_cidade.uf["sigla"],
            "nome": nova_cidade.uf["nome"],
        }
    }

    lista_cidade = get_list_cidades()
    lista_cidade.append(cidade_json)
    set_list_cidades(lista_cidade)