#include <stdio.h>

int main() {
    int monTab[10];
    for (int i = 0; i < 10; i++) {
        printf("Entrez le nombre %d: ", i + 1);
        scanf("%d", &monTab[i]);
    }
    printf("Les nombres saisis sont:\n");
    for (int i = 0; i < 10; i++) {
        printf("%d\n", monTab[i]);
    }
    return 0;
}