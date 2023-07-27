import pytest

############################################################

from main import somar, dividir

############################################################

#Teste de Unidade
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