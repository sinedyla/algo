u0 = float(input("Premier terme u0 : "))
q = float(input("Raison q : "))
n = int(input("Nombre de termes : "))

suite = [u0 * (q ** i) for i in range(n)]
print(f"Suite géométrique : {suite}")