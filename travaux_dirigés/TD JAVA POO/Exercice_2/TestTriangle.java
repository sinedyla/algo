import java.util.Scanner;

public class TestTriangle {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        DessineTriangle triangle = new DessineTriangle();

        int taille = 0;
        int essai = 0;

        while ((taille < 3 || taille > 10) && essai < 3) {
            System.out.print("Donner la taille du triangle : ");
            taille = scanner.nextInt();
            essai++;
        }

        if (essai >=  3) {
            System.out.println("Nombre d'essais dépassé.");
            System.exit(0);
        }

        System.out.println("Vous avez choisi de dessiner un triangle dont le coté mesure "+taille+" lignes.");

        System.out.print("Donner le choix de l'orientation : ");
        int orientation = scanner.nextInt();

        if (orientation == 0) {
            System.out.println("Le programme dessine un triangle orienté vers le bas :");
            triangle.dessineTriangleBas(taille);
        } 
        else if (orientation == 1) {
            System.out.println("Le programme dessine un triangle orienté vers le haut :");
            triangle.dessineTriangleHaut(taille);
        } 
        else {
            System.out.println("Le choix n'existe pas !");
        }
        System.out.println("Merci d'avoir dessiner ce triangle !");
    }
}
