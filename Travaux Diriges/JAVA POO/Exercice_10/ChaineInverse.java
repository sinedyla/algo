// Créer un programme qui permet d’inverser une chaîne de caractères

public class ChaineInverse {
    public String inverseChaine(String s) {
        StringBuilder sb = new StringBuilder(s);
        return sb.reverse().toString();
    }

    public void imprimerChaine(String s) {
        System.out.println("La chaîne inversée est : " + inverseChaine(s));
    }
    public static void main(String[] args) {
        ChaineInverse ci = new ChaineInverse();
        String s = "Bonjour";
        ci.imprimerChaine(s);
    }
}
