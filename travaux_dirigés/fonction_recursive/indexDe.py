"""
Écrire une fonction récursive, appelée indexDe, qui retourne l’index (ou la 
position) si un élément donné est un des éléments d'un tableau d'entiers et -1 
sinon
"""
def indexDe(tab, n, i = 0):
    if i >= len(tab):
        return -1
    if tab[i] == n:
        return i
    return indexDe(tab, n, i + 1)


# Exemple d'utilisation

tableau = [1, 2, 3, 4, 5]
element = 3
index = indexDe(tableau, element)
if index != -1:
    print(f"L'élément {element} se trouve à l'index {index}.")
else:
    print(f"L'élément {element} n'est pas dans le tableau.")
