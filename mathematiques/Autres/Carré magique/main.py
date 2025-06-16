def est_carre_magique(matrice):
    n = len(matrice)

    # 1. Vérifier si c'est un carré (nombre de lignes = nombre de colonnes)
    for ligne in matrice:
        if len(ligne) != n:
            print("Erreur: La matrice n'est pas un carré (nombre de lignes != nombre de colonnes).")
            return False

    if n == 0:
        return False
    constante_magique = sum(matrice[0])

    # 3. Vérifier les sommes des lignes
    for i, ligne in enumerate(matrice):
        if sum(ligne) != constante_magique:
            print(f"La somme de la ligne {i} est différente de la constante magique.")
            return False

    # 4. Vérifier les sommes des colonnes
    for j in range(n):
        somme_colonne = 0
        for i in range(n):
            somme_colonne += matrice[i][j]
        if somme_colonne != constante_magique:
            print(f"La somme de la colonne {j} est différente de la constante magique.")
            return False

    # 5. Vérifier la somme de la diagonale principale
    somme_diag_principale = 0
    for i in range(n):
        somme_diag_principale += matrice[i][i]
    if somme_diag_principale != constante_magique:
        print("La somme de la diagonale principale est différente de la constante magique.")
        return False

    # 6. Vérifier la somme de la diagonale secondaire
    somme_diag_secondaire = 0
    for i in range(n):
        somme_diag_secondaire += matrice[i][n - 1 - i]
    if somme_diag_secondaire != constante_magique:
        print("La somme de la diagonale secondaire est différente de la constante magique.")
        return False


    return True

