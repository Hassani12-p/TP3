def somme(m, n):
    if m >= n:
        return "Erreur!"
    total = 0
    for i in range(m, n + 1):
        total += i
    return total
resultat = somme(9, 12)
print(resultat)