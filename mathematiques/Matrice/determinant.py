import numpy as np

def determinant(matrice):
    """
    Calcule le déterminant d'une matrice carrée.
    """

    if matrice.ndim != 2 or matrice.shape[0] != matrice.shape[1]:
        raise ValueError("La matrice doit être carrée.")

    return np.linalg.det(matrice)


# Exemple d'utilisation
if __name__ == "__main__":
    matrice = np.array([[1, 2], [3, 4]])
    det = determinant(matrice)
    print(f"Le déterminant de la matrice est : {det}")