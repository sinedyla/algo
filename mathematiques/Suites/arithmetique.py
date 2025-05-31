u0 = float(input("Premier terme u0 : "))
r = float(input("Raison r : "))
n = int(input("Nombre de termes : "))

suite = [u0 + i*r for i in range(n)]
print("Suite arithmétique :", suite)