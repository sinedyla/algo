def est_diagonale(matrice):
    """
    Vérifie si une matrice est diagonale.
    Une matrice est diagonale si tous les éléments en dehors de la diagonale principale sont nuls.
    """
    n = len(matrice)
    
    for i in range(n):
        for j in range(n):
            if i != j and matrice[i][j] != 0:
                return False
    return True



matrice = [[1, 0, 0],
           [0, 2, 0],
           [0, 0, 3]]

print(est_diagonale(matrice))

matrice_non_diagonale = [[1, 0, 0],
                          [0, 2, 3],
                          [0, 0, 3]]

print(est_diagonale(matrice_non_diagonale))