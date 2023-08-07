#Bibliotecas

import requests


############################################################


#Variaveis publicas

url = 'https://petstore.swagger.io/v2/pet'
headers = {'Content-Type': 'application/json'}


############################################################


#Definições das Funções (defs)
def teste_incluir_pet():
    #Configura
    ##Dados de entrada provem do pet1.json

    ##Resultado Esperados
    status_cod_esperado = 200
    pet_id_esperado = 1732182
    pet_nome_esperado = "Biscoito"
    pet_nome_categoria_esperado = "cachorro"
    pet_nome_tag_esperado = "vacinado"

    #Executa
    ##Chamar o Método para fazer algo, esse método é o requests.
    resultado_obtido = requests.post(
        url=url,
        headers=headers,
        data=open('C:\\Users\\Cassiano\\PycharmProjects\\pythonProject\\teste_inicio\\vendors\\json\\pet1.json')
    )


    #Valida
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(corpo_do_resultado_obtido)

    assert resultado_obtido.status_code == status_cod_esperado
    assert corpo_do_resultado_obtido['id'] == pet_id_esperado
    assert corpo_do_resultado_obtido['name'] == pet_nome_esperado
    assert corpo_do_resultado_obtido['category']['name'] == pet_nome_categoria_esperado
    assert corpo_do_resultado_obtido['tags'][0]['name'] == pet_nome_esperado