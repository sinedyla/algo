n = int(input("Nombre de termes : "))
suite = [1 / (i+1)**2 for i in range(n)]
somme = sum(suite)

print("Suite :", suite)
print(f"Somme des {n} premiers termes :", somme)