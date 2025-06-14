import numpy as np
def est_triangulaire_superieur(matrice):
    mat = np.array(matrice)
    return np.all(np.tril(mat, k=-1) == 0)



matrice = [[1, 2, 3],
           [0, 5, 6],
           [0, 0, 9]]
print(est_triangulaire_superieur(matrice))