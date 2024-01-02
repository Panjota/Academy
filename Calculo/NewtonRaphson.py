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


def newton_raphson(a, b, k, p):
    aux = 1
    x0 = (a + b) / 2
    f = func(x0)
    df = dfx(x0)
    x1 = x0 - (f / df)
    f1 = func(x1)
    while abs(f1) > float(p) and aux <= k:
        print("k:", aux)
        print("x0: {}".format(x0))
        f = func(x0)
        df = dfx(x0)
        x1 = x0 - (f / df)
        f1 = func(x1)
        print("f(xo)=%.5f" % f)
        print("f'(xo)=%.5f" % df)
        print("x1:%.5f" % x1)
        print("f(x1)=%.5f" % f1)
        x0 = x1
        aux += 1

if __name__ == "__main__":

    a = float(0.1) #float(input("a: "))
    b = float(4) #float(input("b: "))
    k = int(100) #int(input("k: "))
    p = '0.000000001' #input("Precisão: ")
    p2 = p
    inicio = datetime.now()
    newton_raphson(a, b, k, p)
    fim = datetime.now()
    total = fim - inicio
    print(f"Tempo de execução: {total.total_seconds()} segundos")