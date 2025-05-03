# Partie entière supérieure d'un nombre réel


def partie_entiere_superieure(x):
    if x == int(x) :
        return int(x)
    elif x > 0:
        return int(x) + 1
    else:
        return int(x)
    

    
# Exemple d'utilisation
x = 3.7
print("La partie entière de", x, "est", partie_entiere_superieure(x))