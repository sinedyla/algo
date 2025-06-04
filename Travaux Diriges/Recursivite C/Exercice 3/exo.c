// Compter les chiffres d’un entier

#include <stdio.h>

int compterChiffres(int n) {
    if (n == 0) {
        return 0;
    } else {
        return 1 + compterChiffres(n / 10);
    }
}

int main() {
    int n;
    printf("Entrez un entier positif: ");
    scanf("%d", &n);
    printf("Le nombre de chiffres de %d est: %d\n", n, compterChiffres(n));
    return 0;
}