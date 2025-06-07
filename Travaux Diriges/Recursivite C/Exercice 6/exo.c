#include <stdio.h>

int somme_tableau(int arr[], int taille)
{
    if (taille == 0){
        return 0;
    }
    else{
        return arr[taille - 1] + somme_tableau(arr, taille - 1);
    }
}

int main()
{
    int tableau[] = {2, 4, 6, 8, 10};
    int taille = sizeof(tableau) / sizeof(tableau[0]);
    printf("La somme des éléments du tableau est %d\n", somme_tableau(tableau, taille));
    return 0;
}