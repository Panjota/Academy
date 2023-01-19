import re

def _cpf(cpf):
    exp = re.compile("[0-9]{3}[.][0-9]{3}[.][0-9]{3}[-][0-9]{2}")
    a = exp.search(cpf)
    if a:
        validarCpf(cpf)
    else:
        print("False")

def validarCpf(cpf):
    aux = []
    dv1 = int(cpf[13-1])
    dv2 = int(cpf[14-1])
    calcdv1 = 0 #calculo do dv1
    calcdv2 = 0 #calculo do dv2
    mod = 0 #resto da div
    m = 10 #multiplicador

    for i in cpf:
        aux.append(i)
    for e in aux:
        if e == ".":
            aux.remove(e)
        if e == "-":
            aux.remove(e)
    
    #calculo dv1
    for n in aux[:9]:
        n = int(n)
        calcdv1 += n*m
        m -= 1
        mod = calcdv1%11
    if mod < 10: #obs
        calcdv1 = 11 - mod
    else:
        calcdv1 = 0

    #calculo dv2
    m = 11
    for n in aux[:10]:
        n = int(n)
        calcdv2 += n*m
        m -= 1
        mod = calcdv2%11
    if mod >= 10:
        calcdv2 = 0
    else:
        calcdv2 = 11 - mod
        if calcdv2 == 10:
            calcdv2 = 0
    
    if calcdv1 == dv1 and calcdv2 == dv2:
        print("True")
    else:
        print("False")

_cpf()