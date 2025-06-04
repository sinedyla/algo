// Somme des n premiers entiers naturels

#include <stdio.h>

int somme(int n) {
    if (n == 0) {
        return 0;
    } else {
        return n + somme(n - 1);
    }
}

int main() {
    int n;
    printf("Entrez un entier positif: ");
    scanf("%d", &n);
    printf("La somme des %d premiers entiers naturels est: %d\n", n, somme(n));
    return 0;
}