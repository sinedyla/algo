// Écrire une fonction récursive qui compte combien de façons un entier n peut être écrit comme la somme d'entiers positifs ≤ k

#include <stdio.h>

int partition(int n, int k) {
    if (n == 0) return 1;
    if (n < 0 || k == 0) return 0;
    return partition(n - k, k) + partition(n, k - 1);
}

int main() {
    int n = 5;
    int k = 3;
    printf("Nombre de facons d\'ecrire %d comme une somme d\'entiers inferieur ou egal à %d : %d\n", n, k, partition(n, k));
    return 0;
}