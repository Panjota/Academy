# Euclides

m = int(input("m: "))
n = int(input("n: "))
m = m % n
u = m

while True:
    if u == 0:
        print(n)
        break
    else:
        m = n
        n = u

        m = m % n
        u = m