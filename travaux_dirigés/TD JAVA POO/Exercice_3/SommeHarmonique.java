import java.util.Scanner;


public class SommeHarmonique {
    public static double Harmonique(int n) {
        double s = 0.0;
        for (int i = 1; i <= n; i++) {
            s += 1.0 / i;
        }
        return s;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = 0;
        int essai = 0;
        do {
            System.out.println("Veuillez entrer un entier positif : ");
            n = sc.nextInt();
            essai++;
        } while ((n < 1 || n >= 100)  && essai < 5);

        if (n < 1 || n >= 100) {
            System.out.println("Vous avez dépassé le nombre de tentatives.");
            System.exit(0);
        }

        System.out.println("La somme Harmonique des entiers de 1 à "+n+" est : "+ Harmonique(n));
        sc.close();
    }
}


