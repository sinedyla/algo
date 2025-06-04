// Puissance d’un nombre


#include <stdio.h>
int puissance(int base, int exposant) {
    if (exposant == 0) {
        return 1; // Toute base élevée à la puissance 0 est 1
    } else {
        return base * puissance(base, exposant - 1); // Appel récursif
    }
}


int main() {
    int base, exposant;
    printf("Entrez la base: ");
    scanf("%d", &base);
    printf("Entrez l'exposant: ");
    scanf("%d", &exposant);
    printf("%d élevé à la puissance %d est: %d\n", base, exposant, puissance(base, exposant));
    return 0;
}