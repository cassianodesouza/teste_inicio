import pytest


############################################################


def imprimir_oi(nome):
    print(f'Oi, {nome}')


############################################################

# Somar
def somar(numero_a, numero_b):
    return numero_a + numero_b


############################################################


# Subtrair
def subtrair(numero_a, numero_b):
    return numero_a - numero_b


############################################################


# Multiplicar
def multiplicar(numero_a, numero_b):
    return numero_a * numero_b


############################################################


# Dividir
def dividir(numero_a, numero_b):
    try:
        return numero_a / numero_b
    except ZeroDivisionError:
        return 'Não dividiras por zero'


############################################################


if __name__ == '__main__':  # Esse é um IF especial de Python, uma varinha magica, e por isso não muda
    imprimir_oi('Cassiano')

    resultado = somar(5, 7)
    print(f'A soma: {resultado}')


############################################################
# Teste Git
# Escrevendo pelo Git
# Escrevendo pelo Pycharm