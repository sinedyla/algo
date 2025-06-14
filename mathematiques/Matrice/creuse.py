import numpy as np

def est_creuse(matrice):
    """
    Vérifie si une matrice est creuse.
    Une matrice est creuse si la majorité de ses éléments sont nuls.
    """
    mat = np.array(matrice)
    nb_nuls = np.sum(mat == 0)
    # Vérifier si la majorité des éléments sont nuls
    return nb_nuls > (mat.size / 2)



matrice = [[0, 0, 0],
           [0, 2, 0],
           [0, 0, 3]]
print(est_creuse(matrice))

matrice_non_creuse = [[1, 0, 0],
                       [0, 2, 0],
                       [0, 0, 3]]
print(est_creuse(matrice_non_creuse)) 