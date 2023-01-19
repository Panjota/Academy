import re

def _cnpj(cnpj):
    exp = re.compile("[0-9]{2}[.][0-9]{3}[.][0-9]{3}[/][0-9]{4}[-][0-9]{2}")
    a = exp.search(cnpj)
    if a:
        validarCnpj(cnpj)
    else:
        print("False")

def validarCnpj(cnpj):
    aux = []
    dv1 = int(cnpj[17-1])
    dv2 = int(cnpj[18-1])
    calcdv1 = 0 #calculo do dv1
    calcdv2 = 0 #calculo do dv2
    mod = 0 #resto da div
    m = 5 #multiplicador/peso
    for i in cnpj:
        aux.append(i)
    for e in aux:
        if e == ".":
            aux.remove(e)
        if e == "/":
            aux.remove(e)
        if e == "-":
            aux.remove(e)       

    #calculo dv1
    for n in aux[:12]:
        n = int(n)
        calcdv1 += n*m
        m -= 1
        if m == 1:
            m = 9
        mod = calcdv1%11
    if mod < 2:
        calcdv1 = 0
    else:
        calcdv1 = 11 - mod
    
    #calculo dv2
    m = 6
    for n in aux[:13]:
        n = int(n)
        calcdv2 += n*m
        m -= 1
        if m == 1:
            m = 9
        mod = calcdv2%11
    if mod < 2:
        calcdv2 = 0
    else:
        calcdv2 = 11 - mod
    if calcdv1 == dv1 and calcdv2 == dv2:
        print("True")
    else:
        print("False")




_cnpj()