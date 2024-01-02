from datetime import datetime
from math import e, log, pow


def func(x):
    lnx = log(abs(x))
    y = (e**x) - (3 * (x**2)) + lnx
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


def secante(a, b, k, p):
    aux = 1
    x0 = (a+b)/2
    x1 = b

    while aux < k and abs(f):
        x2 =((x0*func(x1))-(x1*func(x0))) / (func(x1) - func(x0))

        print(f"k: {aux} \n x0: {x0} \n x1: {x1} \n x2: {x2}")

        aux += 1



if __name__ == "__main__":

    a = float(input("a: "))
    b = float(input("b: "))
    k = int(input("k: "))
    p = input("Precisão: ")
    p2 = p
    inicio = datetime.now()
    secante(a, b, k, p)
    fim = datetime.now()
    total = fim - inicio
    print(f"Tempo de execução: {total.total_seconds()} segundos")