import numpy as np
def est_triangulaire_inferieure(matrice):
    """
    Vérifie si une matrice est triangulaire inférieure.
    Une matrice est triangulaire inférieure si tous les éléments au dessus de la diagonale principale sont nuls.
    """
    mat = np.array(matrice)
    # Vérifier si tous les éléments au-dessus de la diagonale principale sont nuls
    return np.all(np.triu(mat, k=1) == 0)




matrice = [[1, 0, 0],
           [4, 2, 0],
           [7, 8, 3]]
print(est_triangulaire_inferieure(matrice))

matrice_tri = [[1, 0, 0],
               [4, 2, 0],
               [7, 8, 3]]
print(est_triangulaire_inferieure(matrice_tri))  



