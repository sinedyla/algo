import random

def lancer_de():
    return random.randint(1, 6)


def simuler_lancers(n):
    resultats = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for _ in range(n):
        resultat = lancer_de()
        resultats[resultat] += 1
    return resultats


def calculer_frequence(resultats, n):
    frequence = {}
    for valeur in resultats:
        frequence[valeur] = resultats[valeur] / n
    return frequence

def afficher_resultats(resultats, frequence=None):
    for valeur in sorted(resultats):
        print(f"Nombre de {valeur} : {resultats[valeur]}")
    if frequence:
        print("\nFréquences relatives :")
        for valeur in sorted(frequence):
            print(f"Fréquence de {valeur} : {frequence[valeur]:.2f}")



if __name__ == "__main__":
    n = int(input("Combien de lancers de dé voulez-vous simuler ? "))
    resultats = simuler_lancers(n)
    frequence = calculer_frequence(resultats, n)
    
    afficher_resultats(resultats, frequence)