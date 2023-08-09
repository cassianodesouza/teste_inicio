#Bibliotecas

import requests


############################################################


#Variaveis publicas

url = 'https://petstore.swagger.io/v2/pe'
headers = {'Content-Type: application/json'}


############################################################


#Teste de POST (Enviar)
def teste_incluir_pet():
    #Configura
    ##Dados de entrada provem do pet1.json

    ##Resultado Esperados
    status_code_esperado = 200
    pet_id_esperado = 84808620
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
    print(resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(corpo_do_resultado_obtido)

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['id'] == pet_id_esperado
    assert corpo_do_resultado_obtido['name'] == pet_nome_esperado
    assert corpo_do_resultado_obtido['category']['name'] == pet_nome_categoria_esperado
    assert corpo_do_resultado_obtido['tags'][0]['name'] == pet_nome_tag_esperado


############################################################

#Teste GET (Acessar)
def teste_consultar_pet():
    #Configura
    ##Entrada
    pet_id = '84808620'

    ##Resultado Esperado
    status_code_esperado = 200
    pet_id_esperado = 84808620
    pet_nome_esperado = "Biscoito"
    pet_nome_categoria_esperado = "cachorro"
    pet_nome_tag_esperado = "vacinado"


    #Executa
    resultado_obtido = requests.get(
        url=url + '/' + pet_id,
        headers=headers
    )


    #Valida
    print(resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(corpo_do_resultado_obtido)

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['id'] == pet_id_esperado
    assert corpo_do_resultado_obtido['name'] == pet_nome_esperado
    assert corpo_do_resultado_obtido['category']['name'] == pet_nome_categoria_esperado
    assert corpo_do_resultado_obtido['tags'][0]['name'] == pet_nome_tag_esperado


############################################################


#Teste de PUT (Alterar)
def teste_alterar_pet():
    #Configura
    ##Dados Entrada
    ###Virão do pet2.json

    ##Resultado Esperado
    status_code_esperado = 200
    pet_id_esperado = 84808620
    pet_nome_esperado = "Biscoito"
    pet_nome_categoria_esperado = "cachorro"
    pet_nome_tag_esperado = "vacinado"
    pet_status_esperado = 'pending'

    #Executa
    resultado_obtido = requests.put(
        url=url,
        headers=headers,
        data=open('C:\\Users\\Cassiano\\PycharmProjects\\pythonProject\\teste_inicio\\vendors\\json\\pet2.json')
    )

    #Valida
    print(resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(corpo_do_resultado_obtido)

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['id'] == pet_id_esperado
    assert corpo_do_resultado_obtido['name'] == pet_nome_esperado
    assert corpo_do_resultado_obtido['category']['name'] == pet_nome_categoria_esperado
    assert corpo_do_resultado_obtido['tags'][0]['name'] == pet_nome_tag_esperado
    assert corpo_do_resultado_obtido['status'] == pet_status_esperado