# Recherche lineaire d'un élément dans une liste

def recherche_lineaire(liste, element):
    for i in range(len(liste)):
        if liste[i] == element:
            return True
    return False


# Exemple d'utilisation

liste = [9, 3, 5, 6, 2, 1, 4, 8, 7]
element = 4
print("Liste: ", liste)
print("Element à rechercher: ", element)
print("Resultat de la recherche lineaire: ", recherche_lineaire(liste, element))