"""
On dit qu’un indice d’équilibre d’un tableau d’entiers est un indice tel que la somme des éléments situés à gauche
de cet indice est égale à la somme des éléments situés à droite. L’élément situé à l’indice lui-même n’est pas 
inclus dans ces deux sommes. Écrivez une fonction nommée indice_equilibre qui prend en paramètre une liste d’entiers
tableau et qui retourne : l’indice d’équilibre (le premier trouvé), ou -1 s’il n’en existe pas.
"""

def indice_equilibre(tableau):
    total = sum(tableau)
    gauche = 0
    for i in range(len(tableau)):
        droite = total - gauche - tableau[i]
        if gauche == droite:
            return i
        gauche += tableau[i]
    return -1


# Exemple d'utilisation
tableau = [1, 2, 3, 4, 6]
print("Tableau: ", tableau)
print("Indice d'équilibre: ", indice_equilibre(tableau))

