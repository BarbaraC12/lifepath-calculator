# 1. Obtenir les information necessaire:
#  - Prenoms(s)
#  - Date de naisssaince dd/mm/aaaa
#  - Nom Pere
#  - Nom Mere 
# 2. Calculs specifique pour chaques pierre
# 3. Reduction
# 4. Trouver les pierres correspondante

import utils as u

# 1 La pierre de base
# C’est la première pierre de votre bracelet chemin de vie. Elle représente vos sources, votre enracinement sur terre. Cette pierre permet la canalisation de vos émotions, de vos sentiments. Elle permet de contrôler votre énergie pour que vous avanciez en toute confiance.

# Elle représente le fondement de votre vie. C’est la pierre angulaire qu’il faut, pour que vous ne vous perdiez pas en chemin.

# Méthode de Calcul :

# Pour la trouver, calculez la somme des premières lettres de vos noms et prénoms.
# Exemple : Christine Sophie Dupond Lopez
# C + S + D + L donne 3 + 1 +4 + 3 = 11

def calcul_base(liste):
    somme = 0
    for word in liste:
        somme += u.tableau_de_vie_to_chiffre(word[0])
    return somme

# 2 La pierre de sommet
# La pierre de sommet représente la pierre de votre élévation spirituelle. Elle va de pair, avec votre idéal de vie et avec vos objectifs.

# Méthode de Calcul :  

# Il suffit de calculer les dernières lettres de vos noms et prénoms pour la trouver.
# Exemple : Christine Sophie Dupond Lopez
# E + E + D + Z donne 5 + 5 + 4 + 8 = 22

def calcul_sommet(liste):
    somme = 0
    for word in liste:
        somme += u.tableau_de_vie_to_chiffre(word[-1])
    return somme

# 3 La pierre chemin de vie
# Elle représente la distance à effectuer pour atteindre le sommet. Grâce à elle, vous dépassez vos peurs et vos faiblesses. C’est encore cette pierre qui vous donne de l’intuition et qui vous guide chaque jour de votre vie.

# Méthode de Calcul :

# Elle se calcule grâce à la Somme de votre date de naissance (JJ/MM/AAAA).
# Exemple : 14/09/1963
# 14 + 9 + 1963 = 1986 = 1 + 9 + 8 + 6 = 24

def calcul_chemin_vie(date_naissance):
    jour, mois, annee = map(int, date_naissance.split('.'))
    somme_date = jour + mois + annee
    return somme_date

# 4 La pierre d’appel
# Cette pierre ramène à la surface, les émotions et les blessures profondes. Elle vous permet d’en prendre conscience afin de vous en défaire définitivement. Elle sert à dénouer les nœuds gordiens.

# Méthode de Calcul :

# La somme des voyelles de vos noms et prénoms permet de la trouver.
# Exemple : Christine Sophie Dupond Lopez
# I + I + E + O + I + E + U + O + O + E
# Cela donne 9 + 9 + 5 + 6 + 9 + 5 + 3 + 6 + 6 = 58
# 58 est supérieur à 33 donc 58 => 5 + 8 = 13

def calcul_appel(liste):
    somme = 0
    voyelles = 'AEIOUY'
    for word in liste:
        for letter in word:
            if letter.upper() in voyelles:
                somme += u.tableau_de_vie_to_chiffre(letter)
    return somme

# 5 La pierre de personnalité
# C'est la pierre qui représente le mental. Elle offre un apaisement à votre égo et vous permet d’affronter les obstacles devant vous. C’est aussi la pierre de l’intelligence et de l’expression. De plus, elle révèle votre aspect féminin et masculin et vous enseigne l’art de vivre avec eux.

# Méthode de Calcul :

# Pour la trouver, calculez la Somme des consonnes de vos noms et prénoms.
# Exemple : Christine Sophie Dupond Lopez
# C + H + R + S + T + N + S + P + H + D + P + N + D + L + P + Z
# Cela donne : 3 + 8 + 9 + 1 + 2 + 5 + 1 + 7 + 8 + 4 + 5 + 7 + 4 + 3 + 7 + 8 = 82
# 82 est supérieur à 33 donc 82 => 8 + 2 = 10

def calcul_personnalite(liste):
    somme = 0
    voyelles = 'AEIOUY'
    for word in liste:
        for letter in word:
            if letter.upper() in voyelles:
                somme += 0
            else:
                somme += u.tableau_de_vie_to_chiffre(letter)
    return somme

# 6 La pierre d’expression
# C’est la pierre de la communication. Elle vous permet de vous affirmer, de prendre confiance et de prendre la place qui vous revient dans le monde. Elle participe à l’amélioration de vos relations avec l’extérieur.

# Méthode de Calcul :

# Pour la trouver, faites la Somme des résultats non réduits des 2 pierres précédentes.
# Exemple : 
# Pierre d’Appel non réduit = 58
# Pierre de Personnalité non réduit = 82
# Soit 58 + 82 = 140
# Réduisez 140, soit : 1 + 4 + 0 = 5 des consonnes de vos noms et prénoms.
# Exemple : Christine Sophie Dupond Lopez
# C + H + R + S + T + N + S + P + H + D + P + N + D + L + P + Z
# Cela donne : 3 + 8 + 9 + 1 + 2 

def calcul_expression(a, b):
    return a + b

# 7 La pierre de touche
# C’est la pierre des difficultés. Elle vous offre la lumière et la clarté nécessaire pour que vous preniez de bonnes décisions.

# Méthode de Calcul :

# Pour la trouver, faites la somme de toutes les pierres précédentes (non réduit) à l’exception de celle du chemin de vie. Faites la réduction du résultat obtenu.
# Exemple : 
# Pierre de Base = 11
# Pierre de Sommet = 22
# Pierre d’Appel = 58
# Pierre de Personnalité = 82
# Pierre d’Expression = 140
# Soit 11 + 22 + 58 + 82 + 140 = 313

def calcul_touche(a, b, c, d, e):
    return a + b + c + d + e

# 8 La pierre de vœux
# C’est la pierre qui reflète les émotions de l’être. C’est la pierre de vos désirs, et de l’amour qui siège en vous.

# Méthode de Calcul :

# Elle se calcule par la somme de toutes les premières voyelles de vos noms et prénoms.
# Exemple : Christine Sophie Dupond Lopez
# I + O + U + O = 9 + 6 + 3 + 6 = 24

def calcul_voeux(liste):
    somme = 0
    voyelles = 'AEIOUY'
    for word in liste:
        for letter in word:
            if letter.upper() in voyelles:
                somme += u.tableau_de_vie_to_chiffre(letter)
                break
    return somme

prenoms = input("Entrez vos prenoms au format 'prenom1 prenom2 ...' : ")
nomp = input("Entrez le nom du pere au format 'nom' : ")
nomm = input("Entrez le nom de la mere au format 'nom' : ")
date_naissance = input("Entrez votre date de naissance au format 'JJ.MM.AAAA' : ")
identity = prenoms.split()
identity.append(nomp)
identity.append(nomm)
# Calculer le chemin de vie
chiffre_base = calcul_base(identity)
chiffre_sommet = calcul_sommet(identity)
chiffre_vie = calcul_chemin_vie(date_naissance)
chiffre_appel = calcul_appel(identity)
chiffre_personnalite = calcul_personnalite(identity)
chiffre_expression = calcul_expression(chiffre_appel, chiffre_personnalite)
chiffre_touche = calcul_touche(chiffre_base, chiffre_sommet, chiffre_appel, chiffre_personnalite, chiffre_expression)
chiffre_voeux = calcul_voeux(identity)
print("Vos equivalence de pierre :")

print("\t- Pierre de basee est :", u.somme_chiffres(chiffre_base))
print("\t- Pierre de sommet est :", u.somme_chiffres(chiffre_sommet))
print("\t- Pierre de chemin de vie est :", u.somme_chiffres(chiffre_vie))
print("\t- Pierre d'appel est :", u.somme_chiffres(chiffre_appel))
print("\t- Pierre de personnalite est :", u.somme_chiffres(chiffre_personnalite))
print("\t- Pierre d'expression est :", u.somme_chiffres(chiffre_expression))
print("\t- Pierre de touche est :", u.somme_chiffres(chiffre_touche))
print("\t- Pierre de voeux est :", u.somme_chiffres(chiffre_voeux))

