#include <stdio.h>
int somme_chiffres(int n) {
    if (n == 0) {
        return 0;
    }
    return n % 10 + somme_chiffres(n / 10);
}
int main() {
    int nombre;
    printf("Entrez un entier : ");
    scanf("%d", &nombre);
    
    int resultat = somme_chiffres(nombre);
    printf("La somme des chiffres de %d est %d\n", nombre, resultat);
    
    return 0;
}