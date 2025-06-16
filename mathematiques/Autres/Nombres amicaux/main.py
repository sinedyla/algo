# Deux nombres sont amicaux si la somme des diviseurs propres de l’un est egale à l’autre (et vice-versa).


def somme_diviseurs_propres(n):
    if n < 2:
        return 0
    somme = 1
    for i in range(2, int(n**0.5) + 1) :
        if n % i == 0:
            somme += i
            if i != n // i :
                somme += n // i
    return somme

if __name__ == "__main__":
    a = int(input("Entrez le premier nombre : "))
    b = int(input("Entrez le deuxième nombre : "))

    if a <= 0 or b <= 0:
        print("Les nombres doivent être positifs.")
    else:
        somme_a = somme_diviseurs_propres(a)
        somme_b = somme_diviseurs_propres(b)

        if somme_a == b and somme_b == a:
            print(f"{a} et {b} sont des nombres amicaux.")
        else:
            print(f"{a} et {b} ne sont pas des nombres amicaux.")