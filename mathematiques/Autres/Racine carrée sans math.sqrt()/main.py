# La méthode de Newton-Raphson


def racine_carre(x):
    if x < 0:
        raise ValueError("La racine carrée n'est pas définie pour les nombres négatifs.")
    elif x == 0 or x == 1:
        return x

    approximation = x / 2.0
    tolerance = 1e-10

    while True:
        nouvelle_approximation = (approximation + x / approximation) / 2.0
        if abs(nouvelle_approximation - approximation) < tolerance:
            return nouvelle_approximation
        approximation = nouvelle_approximation