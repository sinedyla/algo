def pgcd(a, b) :
    while b != 0:
        a, b = b, a % b
    return a

def euclide_etendu(a, b) :
    if b == 0:
        return a, 1, 0
    pgcd, x1, y1 = euclide_etendu(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return pgcd, x, y

def inverse_modulaire(a, n) :
    pgcd, x, y = euclide_etendu(a, n)
    if pgcd != 1:
        raise ValueError("L'inverse modulaire n'existe pas.")
    else:
        return x % n