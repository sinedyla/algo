#include <stdio.h>

#define LIGNE 5
#define COLONNES 5

int main() {
    int tableau[LIGNE][COLONNES] = {
        {1, 0, 1, 1, 0},
        {0, 1, 1, 0, 0},
        {1, 1, 1, 1, 1},
        {0, 0, 0, 1, 0},
        {1, 0, 0, 0, 1}
    };
    int ligne_max = 0;
    int max_1 = 0;

    for (int i = 0; i < LIGNE; i++) {
        int compteur_1 = 0;
        for (int j = 0; j < COLONNES; j++) {
            if (tableau[i][j] == 1) {
                compteur_1++;
            }
        }
        if (compteur_1 > max_1) {
            max_1 = compteur_1;
            ligne_max = i;
        }
    }
    printf("La ligne avec le plus grand nombre de 1 est la ligne %d avec %d occurrences de 1.\n", ligne_max + 1, max_1);
    return 0;
}
