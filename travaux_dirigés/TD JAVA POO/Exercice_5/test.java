import java.util.Scanner;

public class test {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Veuillez saisir un entier : ");
        int n = sc.nextInt();
        int essai = 0;
        while ((n < 0 || n > 20) && essai < 2) {
            System.out.println("Ressayez : ");
            n = sc.nextInt();
            essai++;
        }
        if (n < 0 || n > 20) {
            System.out.println("Vous avez depassé le nombre de tentatives.");
            System.exit(0);
        }
        factoriel f = new factoriel();
        f.afficheResultat(n);
    }    
}
