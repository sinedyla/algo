def transposee_matrice(matrice):
    n = len(matrice)
    m = len(matrice[0])
    transposee = []
    for j in range(m):
        ligne_transposee = []
        for i in range(n):
            ligne_transposee.append(matrice[i][j])
        transposee.append(ligne_transposee)
    return transposee

# Exemple d'utilisation
matrice = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrice_transposee = transposee_matrice(matrice)
print(matrice_transposee)