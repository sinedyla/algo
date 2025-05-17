public class factoriel {
    public static int calculFactoriel(int n) {
        int p = 1;
        for (int i = 2; i <= n; i++) {
            p *= i;
        }
        return p;
    }

    public static void afficheResultat(int n) {
        System.out.print("Le factoriel de " + n + " est " + calculFactoriel(n));
    }
}
