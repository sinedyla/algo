import java.util.Scanner;

public class Trinome {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("L'équation est de la forme : ax² + bx + c = 0");
        
        System.out.println("Veuillez saisir la valeur de a : ");
        double a = sc.nextDouble();
        int essai =1;
        while((a==0) && essai <5){
            System.out.println("La valeur de a doit etre different de zero : ");
            a = sc.nextDouble();
            essai++;
        }
        if(a== 0 && essai == 5){
            System.out.println("Vous avez depassé le nombre d'essai !");
            System.exit(0);
        }

        System.out.println("Veuillez saisir la valeur de b : ");
        double b = sc.nextDouble();

        System.out.println("Veuillez saisir la valeur de c : ");
        double c = sc.nextDouble();

        double delta =  Math.pow(b, 2)- 4*a*c;


        if(delta < 0){
            System.out.println("Dans IR, pas de solution!");
            System.out.println("Dans C, L'equation admet deux solution distinctes (x1 et x2) : ");
            System.out.println("X1 = "+(-b/(2*a))+"+"+"i"+Math.sqrt(Math.abs(delta))/(2*a));
            System.out.println("X2 = "+(-b/(2*a))+"-"+"i"+Math.sqrt(Math.abs(delta))/(2*a));
            
        }
        else if(delta == 0){
            System.out.println("Xo ="+(-b/(2*a)));
        }
        else{
            System.out.println("L'equation admet deux solution distinctes (x1 et x2) : ");
            System.out.println("x1 = "+((-b - Math.sqrt(delta))/(2*a)));
            System.out.println("x2 = "+((-b + Math.sqrt(delta))/(2*a)));
        }
    }
}