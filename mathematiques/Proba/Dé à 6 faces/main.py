import random

def lancer_de():
    return random.randint(1, 6)


def simuler_lancers(n):
    resultats = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for _ in range(n):
        resultat = lancer_de()
        resultats[resultat] += 1
    return resultats