def puissance_modulaire_rapide(a, n, p) :
    result = 1
    a = a % p
    while n > 0:
        if (n % 2) == 1 :
            result = (result * a) % p
        n = n // 2
        a = (a * a) % p
    return result

