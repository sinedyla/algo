def colineaires(x1, y1, x2, y2, x3, y3):
    aire = (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
    return aire == 0



# Autre methode utilisant le produit vectoriel

def colineaires_vectoriel(x1, y1, x2, y2, x3, y3) :
    v1x = x2 - x1
    v1y = y2 - y1
    v2x = x3 - x1
    v2y = y3 - y1
    return v1x * v2y == v1y * v2x