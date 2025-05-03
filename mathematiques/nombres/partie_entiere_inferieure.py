# Renvoie la partie entière inferieur d'un nombre réel x.

def partie_entiere_inferieur(x) :
    if x >= 0 :
        return int(x)
    else :
        return int(x) - 1
    

# Exemple d'utilisation
x = - 3.7
print("La partie entière de", x, "est", partie_entiere_inferieur(x))

