// Écrire un programme en C qui affiche la table de multiplication de n. En utilisant la boucle "do-while".
#include <stdio.h>
int main() {
    int n, i = 1;
    printf("Entrez un nombre: ");
    scanf("%d", &n);
    printf("Table de multiplication de %d : \n", n);
    do {
        printf("%d x %d = %d\n", n, i, n * i);
        i++;
    } while (i <= 10);
    
    return 0;
}