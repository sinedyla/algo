package premier;

import java.util.Scanner;

public class TestPoint {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Entrez le premier point");
        System.out.print("x : ");
        float x1 = scanner.nextFloat();
        System.out.print("y : ");
        float y1 = scanner.nextFloat();
        System.out.print("Donnez la couleur en byte : ");
        byte c1 = scanner.nextByte();

        Point p1 = new Point(x1, y1, c1);


        System.out.println("Entrez le deuxieme point");
        System.out.print("x : ");
        float x2 = scanner.nextFloat();
        System.out.print("y : ");
        float y2 = scanner.nextFloat();
        System.out.print("Entrez la couleur en byte : ");
        byte c2 = scanner.nextByte();

        Point p2 = new Point(x2, y2, c2);

        System.out.println("Point 1");
        p1.affiche();

        System.out.println("Point 2");
        p2.affiche();


        if (p1.coïncide(p2)) {
            System.out.println("Les deux points coincident.");
        } else {
            System.out.println("Les deux points ne coincident pas.");
        }

        System.out.println("Entrez les coordonnées du vecteur de translation du Point 1");
        System.out.print("dx : ");
        float dx = scanner.nextFloat();
        System.out.print("dy : ");
        float dy = scanner.nextFloat();
        p1.translater(dx, dy);

        System.out.println("Les nouvelles coordonnées du Point 1");
        p1.affiche();

        scanner.close();
    }
}
