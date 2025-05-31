def verifier_ensembles(nombre):
    ensembles = []
    if nombre >= 0 and nombre == int(nombre):
        ensembles.append("ℕ (naturels)")
        
    if nombre == int(nombre):
        ensembles.append("ℤ (entiers relatifs)")

    ensembles.append("ℚ (rationnels)")
    ensembles.append("ℝ (réels)")

    return ensembles

valeur = input("Entrez un nombre : ")

try:
    nombre = float(valeur)
    ensembles = verifier_ensembles(nombre)
    print(f"\nLe nombre {nombre} appartient aux ensembles suivants : ")
    for e in ensembles:
        print(f"- {e}")
except ValueError:
    print("Entrée invalide. Veuillez entrer un nombre")