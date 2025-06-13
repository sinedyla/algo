import numpy as np


def est_symetrique(matrice):
    """
    Vérifie si une matrice est symétrique.
    Une matrice est symétrique si elle est égale à sa transposée.
    """
    
    if matrice.ndim != 2 or matrice.shape[0] != matrice.shape[1]:
        raise ValueError("La matrice doit être carrée.")
    
    return np.array_equal(matrice, matrice.T)



# Exemple d'utilisation
if __name__ == "__main__":
    matrice = np.array([[1, 2, 3], [2, 4, 5], [3, 5, 6]])
    if est_symetrique(matrice):
        print("La matrice est symétrique.")
    else:
        print("La matrice n'est pas symétrique.")