from datetime import datetime
from math import e, log, pow


def func(x):
    lnx = log(abs(x))
    y = (e ** x) - (3 * (x ** 2)) + lnx
    #y = pow(x, 3) - 5 * pow(x, 2) + 8 * x - 4
    # y = pow(x, 3) - (9 * x) + 3
    return y


def dfx(x):
    h = (pow(e, x) - (6 * x) + 1) / x
    return h


def casas_decimais(p):
    list = []
    for i in p:
        list.append(i)
    list.remove('0')
    list.remove('.')
    digitos = len(list)
    return digitos


def isvalid(a, b):
    try:
        if func(a) * func(b) < 0:
            print(f'Função contínua para o intervalo [{a},{b}]')
            return True
        else:
            print(f'Função não contínua para o intervalo [{a},{b}]')
            return False
    except:
        print("Não foi possível verificar o intevalo")


def falsa_posicao(a, b, k, p):
    aux = 1
    x = (a * func(b) - b * func(a)) / (func(b) - func(a))
    while aux < k and abs(func(x)) > float(p) and abs(b-a) > float(p):
        print(f'k: {aux} \n  a: {a} \n  b: {b} \n  f(a): {func(a)} \n  f(b): {func(b)} '
              f'\n  x: {x} \n  fx: {func(x):.{casas_decimais(p)}f}')
        if func(a)*func(b) < 0:
            a = x
        else:
            b = x
        x = (a * func(b) - b * func(a)) / (func(b) - func(a))

        aux += 1

if __name__ == "__main__":

    a = float(input("a: "))
    b = float(input("b: "))
    k = int(input("k: "))
    p = input("Precisão: ")
    p2 = p
    inicio = datetime.now()
    falsa_posicao(a, b, k, p)
    fim = datetime.now()
    total = fim - inicio
    print(f"Tempo de execução: {total.total_seconds()} segundos")