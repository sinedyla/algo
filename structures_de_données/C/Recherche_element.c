// Recherche d’un élément dans un tableau

#include <stdio.h>
#define TAILLE 10


void recherche(int tab[], int taille, int element) {
    for (int i = 0; i < taille; i++) {
        if (tab[i] == element) {
            printf("L\'element %d a ete trouve à l\'index %d.\n", element, i);
            return;
        }
    }
    printf("L\'element %d n\'a pas ete trouve dans le tableau.\n", element);
}

int main() {
    int tab[TAILLE] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int element;
    printf("Entrez l\'element à rechercher : ");
    scanf("%d", &element);
    recherche(tab, TAILLE, element);

    return 0;
}