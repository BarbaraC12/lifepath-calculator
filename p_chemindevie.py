# La pierre chemin de vie
# Elle représente la distance à effectuer pour atteindre le sommet. Grâce à elle, vous dépassez vos peurs et vos faiblesses. C’est encore cette pierre qui vous donne de l’intuition et qui vous guide chaque jour de votre vie.

# Méthode de Calcul :

# Elle se calcule grâce à la Somme de votre date de naissance (JJ/MM/AAAA).
# Exemple : 14/09/1963
# 14 + 9 + 1963 = 1986 = 1 + 9 + 8 + 6 = 24

def somme_chiffres(nombre):
    while nombre >= 10:
        nombre = sum(int(chiffre) for chiffre in str(nombre))
    return nombre

def calcul_chemin_vie(date_naissance):
    jour, mois, annee = map(int, date_naissance.split('/'))
    somme_date = jour + mois + annee
    resultat_final = somme_chiffres(somme_date)
    return resultat_final