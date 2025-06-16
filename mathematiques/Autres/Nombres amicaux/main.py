# Deux nombres sont amicaux si la somme des diviseurs propres de l’un est egale à l’autre (et vice-versa).


def somme_diviseurs_propres(n):
    if n < 2:
        return 0
    somme = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            somme += i
            if i != n // i :
                somme += n // i
    return somme

