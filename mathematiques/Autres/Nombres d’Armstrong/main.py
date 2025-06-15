def est_armstrong(n):
    puissance = len(str(n))
    somme = sum(int(digit) ** puissance for digit in str(n))
    return somme == n