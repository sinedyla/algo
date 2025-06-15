def crible_eratosthene(n):
    premiers = []
    for i in range(2, n):
        est_premier = True
        for p in premiers:
            if p * p > i:
                break
            if i % p == 0:
                est_premier = False
                break
        if est_premier:
            premiers.append(i)
    return premiers