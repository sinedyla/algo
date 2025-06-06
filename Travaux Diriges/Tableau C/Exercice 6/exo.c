#include <stdio.h>
#include <string.h>
void inverser_chaine(char *chaine, int debut, int fin) {
    if (debut >= fin) {
        return;
    }
    char temp = chaine[debut];
    chaine[debut] = chaine[fin];
    chaine[fin] = temp;
    inverser_chaine(chaine, debut + 1, fin - 1);
}
int main() {
    char chaine[100];
    printf("Entrez une chaîne de caractères : ");
    fgets(chaine, sizeof(chaine), stdin);
    
    // Enlever le caractère de nouvelle ligne sil existe
    size_t len = strlen(chaine);
    if (len > 0 && chaine[len - 1] == '\n') {
        chaine[len - 1] = '\0';
    }
    
    inverser_chaine(chaine, 0, strlen(chaine) - 1);
    
    printf("Chaîne inversée : %s\n", chaine);
    
    return 0;
}