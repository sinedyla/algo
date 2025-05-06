# Additionner deux matrices



def addition_matrices(matrice1, matrice2):
    if len(matrice1) != len(matrice2) and len(matrice1[0]) != len(matrice2[0]):
        print("Les matrices doivent avoir la même taille")
        return None
    matrice_resultat = []
    for i in range(len(matrice1)):
        ligne_resultat = []
        for j in range(len(matrice1[0])):
            ligne_resultat.append(matrice1[i][j] + matrice2[i][j])
        matrice_resultat.append(ligne_resultat)

    return matrice_resultat


# Exemple d'utilisation
matrice1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrice2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

resultat = addition_matrices(matrice1, matrice2)

if resultat != None:
    print("Voici la matrice additionnée :")
    for l in resultat:
        print(l)