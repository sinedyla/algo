import java.util.Scanner;

public class TestCercle {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("--- Les caractéristiques du cercle ---");
        System.out.print("Veuillez saisir le centre du cercle : ");
        String centre = sc.nextLine();
        System.out.print("Veuillez saisir le rayon du cercle : ");
        float rayon = sc.nextFloat();
        Cercle ce = new Cercle(centre, rayon);
        ce.affiche();
        ce.imprime();
    }
}
