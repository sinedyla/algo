#include <stdio.h>

int main() {
    int jours, annees, semaines, jours_restants;

    printf("Entrez le nombre de jours: ");
    scanf("%d", &jours);

    annees = jours / 365;
    jours_restants = jours % 365;
    semaines = jours_restants / 7;
    jours_restants = jours_restants % 7;

    printf("%d jours = %d annees, %d semaines et %d jours\n", jours, annees, semaines, jours_restants);

    return 0;
}