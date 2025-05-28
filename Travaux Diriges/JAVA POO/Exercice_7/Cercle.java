public class Cercle {
    private String centre;
    private float rayon;

    public Cercle(String centre, float rayon) {
        this.centre = centre;
        this.rayon = rayon;
    }

    public double surface() {
        return Math.PI * Math.pow(this.rayon, 2);
    }

    public void affiche() {
        System.out.println("Le cercle a pour centre " + this.centre + " et de rayon " + this.rayon+" cm");
    }

    public void imprime() {
        System.out.println("La surface de ce cercle est " +surface()+" cm²");
    }
}
