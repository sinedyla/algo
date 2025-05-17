package premier;

public class Point {
    private float x;
    private float y;
    private byte couleur;


    public Point(float x, float y) {
        this.x = x;
        this.y = y;
        this.couleur = 0;
    }

    public Point(float x, float y, byte couleur) {
        this(x, y);
        this.couleur = couleur;
    }

    // Point d'origine
    public Point() {
        this(0, 0);
    }

    public void translater(float dx, float dy) {
        this.x += dx;
        this.y += dy;
    }


    public void affiche() {
        System.out.println("x = " + x + ", y = " + y + ", couleur = " + couleur);
    }

    public boolean coïncide(Point p) {
        return this.x == p.x && this.y == p.y;
    }
}
