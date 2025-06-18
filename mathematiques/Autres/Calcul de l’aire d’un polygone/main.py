def aire_polygone(coordonnees) :
    n = len(coordonnees)
    if n < 3:
        raise ValueError("Un polygone doit avoir au moins 3 sommets")
    
    aire = 0
    for i in range(n) :
        x1, y1 = coordonnees[i]
        x2, y2 = coordonnees[(i + 1) % n]
        aire += x1 * y2 - x2 * y1
    
    return abs(aire) / 2


