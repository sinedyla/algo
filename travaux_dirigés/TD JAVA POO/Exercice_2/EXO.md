# Exercice 2

On veut réaliser un programme (une classe `DessineTriangle`) qui dessine :

- un triangle rectangle orienté vers le haut comme suit :

`*  `
`* *  `
`* * *  `
`* * * *  `
`* * * * * `


- un triangle rectangle orienté vers le bas comme suit :

`* * * * *`
  `* * * * `
   ` * * * `
     ` * *`
       ` *`


### NB :
Vous utiliserez des astérisques pour représenter les côtés du triangle.  
On prévoit deux méthodes dans cette classe :

- `public void dessineTriangleBas(int m) :` cette méthode permettra de dessiner le triangle orienté vers le bas. Le paramètre `m` passé en argument à la méthode sera la taille du tableau.
- `public void dessineTriangleHaut(int n) :` pour dessiner le triangle orienté vers le haut.

Créer ensuite une seconde classe principale `TestTriangle` pour tester le code ci-dessus.

On imposera à l’utilisateur de saisir une taille comprise entre 3 et 10 et l’utilisateur n’a droit qu’à 3 essais au maximum pour donner une valeur acceptable. Passé ce nombre, on met fin à l’exécution du programme (on peut utiliser pour cela `System.exit(0)`).

Le choix de l’orientation du triangle sera la valeur 0 pour dessiner vers le bas et la valeur 1 pour dessiner vers le haut. Le choix sera aussi demandé à l’utilisateur.

L’exécution de votre programme sera comme suit :

Donner la taille du triangle : 5
Vous avez choisi de dessiner un triangle dont le côté mesure 5 lignes
Donner le choix de l'orientation : 1
Le programme dessine un triangle orienté vers le haut :

`*  `
`* *  `
`* * *  `
`* * * *  `
`* * * * * `