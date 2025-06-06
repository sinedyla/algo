#include <stdio.h>
#include <string.h>

int est_palindrome(char *mot, int debut, int fin) {
    if (debut >= fin) {
        return 1;
    }
    if (mot[debut] != mot[fin]) {
        return 0;
    }
    return est_palindrome(mot, debut + 1, fin - 1);
}

int main() {
    char mot[100];

    printf("Entrez un mot : ");
    scanf("%s", mot);

    if (est_palindrome(mot, 0, strlen(mot) - 1)) {
        printf("%s est un palindrome.\n", mot);
    } else {
        printf("%s n'est pas un palindrome.\n", mot);
    }
    return 0;
}