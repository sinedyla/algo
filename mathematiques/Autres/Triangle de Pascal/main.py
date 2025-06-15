def triangle_de_pascal(n):
    triangle = []
    for i in range(n):
        ligne = [1] * (i + 1)
        for j in range(1, i):
            ligne[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(ligne)
    return triangle

