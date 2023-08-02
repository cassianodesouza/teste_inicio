import csv

import pytest


############################################################


from main import somar, dividir, subtrair, multiplicar


############################################################


#Definição para Leitura do CSV de Teste em Massa
def ler_csv(arquivo_csv):
    dados_csv = []
    try:
        with open(arquivo_csv, newline='') as massa:
            campos = csv.reader(massa, delimiter=',')
            next(campos)
            for linha in campos:
                dados_csv.append(linha)
        return dados_csv
    except FileNotFoundError:
        print(f'Arquivo não encontrado: {arquivo_csv}')
    except Exception as fail:
        print(f'Falha imprevista: {fail}')


############################################################


#Teste de Unidade - Somar
def teste_somar():
    # 1- Configura
    numero_a = 8
    numero_b = 7
    resultado_esperado = 15

    # 2- Executa
    resultado_obtido = somar(numero_a, numero_b)

    #3 - Valida
    assert resultado_obtido == resultado_esperado


############################################################


#Teste de Unidade - Subtrair
def teste_subtrair():
    # 1- Configura
    numero_a = 15
    numero_b = 10
    resultado_esperado = 5

    # 2- Executa
    resultado_obtido = subtrair(numero_a, numero_b)

    #3 - Valida
    assert resultado_obtido == resultado_esperado


############################################################


#Teste de Unidade - Subtrair Massa CSV
@pytest.mark.parametrize('numero_a, numero_b, resultado_esperado',ler_csv('C:\\Users\\Cassiano\PycharmProjects\pythonProject\\teste_inicio\\vendors\\CSV\\massa_teste_subtrair_positivo.csv'))
def teste_subtrair_leitura_csv(numero_a, numero_b, resultado_esperado):
    # 1- Configura

    # 2- Executa
    resultado_obtido = subtrair(int(numero_a), int(numero_b))

    #3 - Valida
    assert resultado_obtido == int(resultado_esperado)


############################################################


#Teste de Unidade - Multilicar Massa CSV
@pytest.mark.parametrize('numero_a, numero_b, resultado_esperado',ler_csv('C:\\Users\\Cassiano\\PycharmProjects\\pythonProject\\teste_inicio\\vendors\\CSV\\massa_teste_multiplicar_positivo.csv'))
def teste_multiplicar_leitura_csv(numero_a, numero_b, resultado_esperado):
    # 1- Configura

    # 2- Executa
    resultado_obtido = multiplicar(int(numero_a), int(numero_b))

    #3 - Valida
    assert resultado_obtido == int(resultado_esperado)


############################################################


#Teste Positivo
def teste_dividir_positivo():
    #1-Configura
    #1.1- Dados de Entrada
    numero_a = 27
    numero_b = 3

    #1.2- Resultados Esperados
    resultado_esperado = 9

    #2-Executa
    resultado_obtido = dividir(numero_a, numero_b)

    #3-Valida
    assert resultado_obtido == resultado_esperado


############################################################


#Teste Negativo
def teste_dividir_negativo():
    #1-Configura
    #1.1- Dados de Entrada
    numero_a = 27
    numero_b = 0

    #1.2- Resultados Esperados
    resultado_esperado = 'Não dividiras por zero'

    #2-Executa
    resultado_obtido = dividir(numero_a, numero_b)

    #3-Valida
    assert resultado_obtido == resultado_esperado


############################################################


#Teste Somar Massificado

#Lista para uso como massa de testes
lista_de_valores = [
    (8, 7, 15),
    (20, 30, 50),
    (25, 0, 25),
    (-5, 12, 7),
    (6, -3, 3)
]


#Vincular a lista com o teste
@pytest.mark.parametrize('numero_a, numero_b, resultado_esperado', lista_de_valores)

#Teste Massivo a ser aplicado
def teste_somar_leitura_de_lista(numero_a, numero_b, resultado_esperado):
    # 1- Configura
    # Utilizamos os dados na Lista de Valores como massa de teste

    # 2- Executa
    resultado_obtido = somar(numero_a, numero_b)

    #3 - Valida
    assert resultado_obtido == resultado_esperado


############################################################


#Teste de Unidade - Subtrair Massa CSV
@pytest.mark.parametrize('numero_a, numero_b, resultado_esperado', ler_csv('C:\\Users\\Cassiano\\PycharmProjects\\pythonProject\\teste_inicio\\vendors\\CSV\\massa_teste_somar_positivo.csv'))
def teste_somar_leitura_de_csv(numero_a, numero_b, resultado_esperado):
    # 1- Configura
    # Utilizamos os dados na Lista de Valores como massa de teste

    # 2- Executa
    resultado_obtido = somar(int(numero_a), int(numero_b))

    #3 - Valida
    assert resultado_obtido == int(resultado_esperado)


############################################################