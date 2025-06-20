import random
def lancer_piece():
    return random.choice(['face', 'pile'])

def simuler_lancers(n):
    resultats = {'face': 0, 'pile': 0}
    for _ in range(n):
        resultat = lancer_piece()
        resultats[resultat] += 1
    return resultats
