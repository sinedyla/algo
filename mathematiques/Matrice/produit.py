"""
Produit de deux matrices.
"""

import numpy as np

def produit_matrice(A, B):
    return np.dot(A, B)





# Exemple d'utilisation
if __name__ == "__main__":
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    C = produit_matrice(A, B)
    print("Produit de A et B : ")
    print(C)