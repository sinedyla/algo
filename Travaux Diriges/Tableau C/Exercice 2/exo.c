#include <stdio.h>

int main() {
    float notes[10];
    float somme = 0.0;
    for (int i = 0; i < 10; i++) {
        printf("Entrez la note %d: ", i + 1);
        scanf("%f", &notes[i]);
        somme += notes[i];
    }
    printf("La moyenne des notes est: %.2f\n", somme / 10);
    return 0;
}