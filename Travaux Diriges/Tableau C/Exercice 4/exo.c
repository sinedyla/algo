#include <stdio.h>
int main() {
    int monTab[10];
    int temp;
    for (int i = 0; i < 10; i++) {
        printf("Entrez le nombre %d : ", i + 1);
        scanf("%d", &monTab[i]);
    }
    for (int i = 0; i < 10 - 1; i++) {
        for (int j = 0; j < 10 - i - 1; j++) {
            if (monTab[j] > monTab[j + 1]) {
                temp = monTab[j];
                monTab[j] = monTab[j + 1];
                monTab[j + 1] = temp;
            }
        }
    }
    printf("Le tableau trié est : \n");
    for (int i = 0; i < 10; i++) {
        printf("%d\n", monTab[i]);
    }
    return 0;
}