#include <stdio.h>
#include <string.h>

/**
 * Programme de bienvenue simple
 * Un premier programme pour apprendre les bases du C
 */

void dire_bonjour() {
    printf("Bonjour ! 👋\n");
    printf("Bienvenue dans ce dépôt d'apprentissage d'algorithmes !\n");
    printf("Hello! Welcome to this algorithm learning repository!\n");
}

void dire_bonjour_personnalise(char *nom) {
    printf("Bonjour %s ! 👋\n", nom);
    printf("Ravi de vous voir ici !\n");
}

int main() {
    char nom[100];
    
    // Message de bienvenue simple
    dire_bonjour();
    printf("\n");
    
    // Demander le nom de l'utilisateur
    printf("Comment vous appelez-vous ? ");
    
    if (fgets(nom, sizeof(nom), stdin) != NULL) {
        // Enlever le caractère de nouvelle ligne si présent
        size_t len = strlen(nom);
        if (len > 0 && nom[len - 1] == '\n') {
            nom[len - 1] = '\0';
        }
        
        if (strlen(nom) > 0) {
            printf("\n");
            dire_bonjour_personnalise(nom);
        }
    }
    
    return 0;
}
