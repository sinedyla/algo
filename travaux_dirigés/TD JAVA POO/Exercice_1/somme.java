import java.util.Scanner;

/*
Créer un programme qui permet de calculer et d’afficher la somme 
de deux entiers donnés par l’utilisateur.
 */
 
 public class somme {
     public static void main(String[] args) {
         Scanner sc = new Scanner(System.in);
         System.out.println("Veuillez saisir la valeur de A : ");
         String A = sc.nextLine();
         System.out.println("Veuillez saisir la valeur de B : ");
         String B = sc.nextLine();
         int a = Integer.parseInt(A);
         int b = Integer.parseInt(B);
         int S = a + b;
         System.out.println("A + B = "+S);
     }
 }