#include <stdio.h>
int puissance(int base, int exposant) {
    if (exposant == 0) {
        return 1;
    } else if (exposant < 0) {
        return 1 / puissance(base, -exposant);
    } else {
        return base * puissance(base, exposant - 1);
    }
}

int main() {
    int base, exposant;
    printf("Entrez la base : ");
    scanf("%d", &base);
    printf("Entrez l'exposant : ");
    scanf("%d", &exposant);
    
    int resultat = puissance(base, exposant);
    printf("%d élevé à la puissance %d est %d\n", base, exposant, resultat);
    
    return 0;
}