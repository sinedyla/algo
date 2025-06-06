#include <stdio.h>
int main() {
    int monTab[10];
    int max = 0;
    for (int i = 0; i < 10; i++) {
        printf("Entrez le nombre %d : ", i + 1);
        scanf("%d", &monTab[i]);
        if (i == 0 || monTab[i] > max) {
            max = monTab[i];
        }
    }
    printf("Le maximum des nombres saisis est : %d\n", max);
    return 0;
}