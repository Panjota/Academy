from datetime import datetime
from math import e, log
from time import sleep


def fx(x):
    lnx = log(abs(x))
    f = (e ** x) - (3 * (x ** 2)) + lnx
    return f


def dfx(x):
    h = (e ** x) - 6 * x + 1 / x
    return h


def isvalid(a, b):
    try:
        if fx(a) * fx(b) < 0:
            print(f'Função contínua para o intervalo [{a},{b}]')
            return True
        else:
            print(f'Função não contínua para o intervalo [{a},{b}]')
            print('Entre com os valores iniciais novamente.')
            return False
    except:
        print("Não foi possível verificar o intevalo")
        print('Entre com os valores iniciais novamente.')


##METODO DA BISSECAO
def bisseccao(a, b, p, k):
    i = 1
    x = (a + b) / 2
    f = fx(x)

    while abs(f) > p and i <= k:
        x = (a + b) / 2
        f = fx(x)
        M = fx(a)

        print(f'k: {i} \n a: {a} b: {b} x: {x} f(x):{f:.12f}')

        if ((M * f) > 0):
            a = x
        else:
            b = x
        i = i + 1


##METODO DO FALSA POSICAO


def falsa_posicao(a, b, p, k):
    i = 1
    if fx(a) * fx(b) < 0:
        xo = (a * fx(b) - b * fx(a)) / (fx(b) - fx(a))
        while (abs(fx(xo))) > p and i <= k:
            if fx(a) * fx(b) < 0:
                a = xo
            else:
                b = xo

            print(f'k: {i} \n x0: {xo:.12f}')

            xo = (a * fx(b) - b * fx(a)) / (fx(b) - fx(a))

            print(f'x1: {xo:.12f} g(x1): {xo:.12f} f(x): {fx(xo):.12f}')
            i = i + 1


##METODO NEWTON-RAPHSON


def newton(a, b, p, k):
    i = 1
    xo = (a + b) / 2
    f = fx(xo)
    df = dfx(xo)
    x1 = xo - (f / df)
    f1 = fx(x1)

    while abs(f1) > p and i <= k:
        print(f'k: {i} \n x0: {xo:.12f}')
        f = fx(xo)
        df = dfx(xo)
        x1 = xo - (f / df)
        f1 = fx(x1)

        print(f'x0: {f:.12f} d(x0): {df:.12f} x1: {x1:.12f} f(x1): {f1:.12f}')

        xo = x1
        i = i + 1


# Metodo da Secante


def secante(a, b, p, k):
    i = 1
    xo = a
    x1 = b
    f0 = fx(xo)
    f1 = fx(x1)

    while abs(f1) > p and i <= k:
        print(f'k: {i} \n x0: {xo:.12f}')
        df = (f1 - f0) / (x1 - xo)
        x2 = x1 - f1 / df
        f2 = fx(x2)

        print(f'x0: {f1:.12f} d(x0): {df:.12f} x1: {x2:.12f} f(x1): {f2:.12f}')

        xo, x1 = x1, x2
        f0, f1 = f1, f2
        i += 1


##COMPARAR OS METODOS
def comparar_metodos(a, b, p, k):
    pass


print("Programa:Zero de função")
print("f(x)=e^x-3x^2+ln(x)")

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
p = float(input("Digite o valor da precisão: "))
k = int(input("Digite o valor de k: "))
while not isvalid(a, b):
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    p = float(input("Digite o valor da precisão: "))
    k = int(input("Digite o valor de k: "))

while True:
    sleep(3)
    print("OPÇÕES:")
    print("[1] - Bisseção")
    print("[2] - Falsa Posição")
    print("[3] - Newton-Raphson")
    print("[4] - Secante")
    print("[5] - Mudar valores")
    print("[6] - Sair")

    opc = int(input(("O que deseja fazer?")))
    if opc == 1:
        print("Método da bisseção")
        inicio = datetime.now()
        bisseccao(a, b, p, k)
        fim = datetime.now()
        total = fim - inicio
        print(f"Tempo de execução: {total.total_seconds()} segundos")

    elif opc == 2:
        print("Método da Falsa Posição")
        inicio = datetime.now()
        falsa_posicao(a, b, p, k)
        fim = datetime.now()
        total = fim - inicio
        print(f"Tempo de execução: {total.total_seconds()} segundos")

    elif opc == 3:
        print("Método de Newton-Raphson")
        inicio = datetime.now()
        newton(a, b, p, k)
        fim = datetime.now()
        total = fim - inicio
        print(f"Tempo de execução: {total.total_seconds()} segundos")

    elif opc == 4:
        print("Método da secante")
        inicio = datetime.now()
        secante(a, b, p, k)
        fim = datetime.now()
        total = fim - inicio
        print(f"Tempo de execução: {total.total_seconds()} segundos")

    elif opc == 5:
        while True:
            a = float(input("Digite o valor de a: "))
            b = float(input("Digite o valor de b: "))
            p = float(input("Digite o valor da precisão: "))
            k = int(input("Digite o valor de k: "))
            if isvalid(a, b):
                break

    elif opc == 6:
        break
    else:
        print("")
        print("Opção inválida")
