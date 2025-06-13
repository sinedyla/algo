import numpy as np


def egalite_matrices(A, B):
    """
    Verifie si deux matrices A et B sont egales.
    """
    return np.array_equal(A, B)



# Exemple d'utilisation
if __name__ == "__main__":
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[1, 2], [3, 4]])
    C = np.array([[5, 6], [7, 8]])
    
    print("A et B sont egales : ", egalite_matrices(A, B))
    print("A et C sont egales : ", egalite_matrices(A, C))