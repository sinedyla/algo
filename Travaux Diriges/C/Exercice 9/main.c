// Écrire un programme en C pour afficher tous les éléments uniques dans un tableau non trié.
#include <stdio.h>
#include <stdbool.h>

#define TAILLE 100

int main() {
    int tableau[TAILLE];
    int n;

    printf("Entrez le nombre d'elements dans le tableau : ");
    scanf("%d", &n);

    printf("Entrez les elements du tableau : \n");
    for (int i = 0; i < n; i++) {
        scanf("%d", &tableau[i]);
    }
    printf("Les elements uniques du tableau sont : ");
    for (int i = 0; i < n; i++) {
        bool est_unique = true;
        for (int j = 0; j < n; j++) {
            if (i != j && tableau[i] == tableau[j]) {
                est_unique = false;
                break;
            }
        }
        if (est_unique) {
            printf("%d ", tableau[i]);
        }
    }
    printf("\n");
    return 0;
}
