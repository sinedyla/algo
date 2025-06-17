# Nombre de chemins dans une grille

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)


def chemins(n, m):
    return fact(n + m) // (fact(n) * fact(m))




