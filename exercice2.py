import math;
def delta(a, b, c):
    return b**2 - 4*a*c

def NombreRacine(a, b, c):
    discriminant = delta(a, b, c)
    if discriminant > 0:
        return 2
    elif discriminant == 0:
        return 1
    else:
        return 0

def AfficheNombreRacine(a, b, c):
    nb_solutions = NombreRacine(a, b, c)
    if nb_solutions == 2:
        print("L'équation a deux solutions.")
    elif nb_solutions == 1:
        print("L'équation a une solution.")
    else:
        print("L'équation n'a pas de solution réelle.")


def Racine1(a, b, c):
    discriminant = delta(a, b, c)
    if discriminant >= 0:
        return (-b + math.sqrt(discriminant)) / (2*a)
    else:
        return 0

def Racine2(a, b, c):
    discriminant = delta(a, b, c)
    if discriminant >= 0:
        return (-b - discriminant**0.5) / (2*a)
    else:
        return None

def conversion_temps(h, m, s):
    return h * 3600 + m * 60 + s

def temps_ecoule(h1, m1, s1, h2, m2, s2):
    temps1 = conversion_temps(h1, m1, s1)
    temps2 = conversion_temps(h2, m2, s2)
    return abs(temps2 - temps1)

def conversion_distance(km, m, cm):
    return km * 1000 + m + cm / 100

def vitesse(distance, temps):
    return distance / temps if temps != 0 else None


a, b, c = 1, -3, 2
AfficheNombreRacine(a, b, c)
print("Racine 1:", Racine1(a, b, c))
print("Racine 2:", Racine2(a, b, c))

temps1 = (1, 30, 0)
temps2 = (2, 15, 30)
distance = (2, 500, 50)
temps_ecoule = temps_ecoule(*temps1, *temps2)
distance_m = conversion_distance(*distance)
vitesse_ms = vitesse(distance_m, temps_ecoule)

print("Temps écoulé entre les deux horaires:", temps_ecoule, "secondes")
print("Distance en mètres:", distance_m, "mètres")
print("Vitesse moyenne:", vitesse_ms, "m/s")
