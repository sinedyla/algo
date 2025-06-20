import random
def lancer_piece():
    return random.choice(['face', 'pile'])

def simuler_lancers(n):
    resultats = {'face': 0, 'pile': 0}
    for _ in range(n):
        resultat = lancer_piece()
        resultats[resultat] += 1
    return resultats

def calculer_frequence(resultats, n):
    frequence = {}
    frequence['face'] = resultats['face'] / n
    frequence['pile'] = resultats['pile'] / n
    return frequence


def afficher_resultats(resultats, frequence=None):
    print(f"Nombre de faces : {resultats['face']}")
    print(f"Nombre de piles : {resultats['pile']}")
    if frequence:
        print(f"Fréquence relative des faces : {frequence['face']:.2f}")
        print(f"Fréquence relative des piles : {frequence['pile']:.2f}")

