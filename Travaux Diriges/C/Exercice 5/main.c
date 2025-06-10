#include <stdio.h>
int main() {
    int a, b, temp;
    int x,y;

    printf("Entrez le premier nombre: ");
    scanf("%d", &a);
    printf("Entrez le second nombre: ");
    scanf("%d", &b);

    x = a;
    y = b;
    while (y != 0) {
        temp = y;
        y = x % y;
        x = temp;
    }
    printf("PGCD(%d,%d) = %d\n", a, b, x);

    return 0;
}