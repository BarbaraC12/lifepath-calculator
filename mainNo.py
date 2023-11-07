import utils as u


def calcul_base(liste) -> int:
    """
    Calcule la pierre de base.

    C’est la première pierre de votre bracelet chemin de vie.
    Elle représente vos sources, votre enracinement sur terre.
    Cette pierre permet la canalisation de vos émotions, de vos sentiments.
    Elle permet de contrôler votre énergie pour que vous avanciez
    en toute confiance.

    Méthode de Calcul :
        Il suffit de calculer les premières lettres des noms et prénoms.
    Args:
        liste (list): Une liste de noms et prénoms
    Returns:
        int: La valeur de la pierre de base calculée
    """
    somme = 0
    for word in liste:
        somme += u.tableau_de_vie_to_chiffre(word[0])
    return somme


def calcul_sommet(liste) -> int:
    """
    Calcule la pierre de sommet.

    La pierre de sommet représente la pierre de votre élévation spirituelle.
    Elle va de pair, avec votre idéal de vie et avec vos objectifs.

    Méthode de Calcul :
        On l'obtient en additionnant les dernières lettres des noms et prénoms.
    Args:
        liste (list): Une liste de noms et prénoms.
    Returns:
        int: La valeur de la pierre de sommet.
    """
    somme = 0
    for word in liste:
        somme += u.tableau_de_vie_to_chiffre(word[-1])
    return somme


def calcul_chemin_vie(date_naissance) -> int:
    """
    Calcule la pierre chemin de vie.

    Elle représente la distance à effectuer pour atteindre le sommet.
    Grâce à elle, vous dépassez vos peurs et vos faiblesses.
    C’est encore cette pierre qui vous donne de l’intuition et qui vous guide
    chaque jour de votre vie.

    Méthode de Calcul :
        Elle se calcule grâce à la Somme de la date de naissance (JJ/MM/AAAA).
    Args:
        date_naissance (str): La date de naissance au format JJ/MM/AAAA.
    Returns:
        int: La valeur de la pierre chemin de vie.
    """
    jour, mois, annee = u.split_date(date_naissance)
    somme_date = jour + mois + annee
    return somme_date


def calcul_appel(liste) -> int:
    """
    Calcule la pierre d’appel.

    Cette pierre ramène à la surface, les émotions et les blessures profondes.
    Elle vous permet d’en prendre conscience afin de vous en défaire
    définitivement. Elle sert à dénouer les nœuds gordiens.

    Méthode de Calcul:
        La somme des voyelles de vos noms et prénoms permet de la trouver.
    Args:
        liste (list): Une liste de noms et prénoms.

    Returns:
        int: La valeur de la pierre d’appel.
    """
    somme = 0
    voyelles = 'AEIOUY'
    for word in liste:
        for letter in word:
            if letter.upper() in voyelles:
                somme += u.tableau_de_vie_to_chiffre(letter)
    return somme


def calcul_personnalite(liste) -> int:
    """
    Calcule la pierre de personnalité.

    C'est la pierre qui représente le mental. Elle offre un apaisement à votre
    égo et vous permet d’affronter les obstacles devant vous. C’est aussi la
    pierre de l’intelligence et de l’expression. De plus, elle révèle votre
    aspect féminin et masculin et vous enseigne l’art de vivre avec eux.

    Méthode de Calcul :
        Pour la trouver, calculez la Somme des consonnes des noms et prénoms.
    Args:
        liste (list): Une liste de noms et prénoms.
    Returns:
        int: La valeur de la pierre de personnalité.
    """
    somme = 0
    voyelles = 'AEIOUY'
    for word in liste:
        for letter in word:
            if letter.upper() in voyelles:
                somme += 0
            else:
                somme += u.tableau_de_vie_to_chiffre(letter)
    return somme


def calcul_expression(a, b) -> int:
    """
    Calcule la pierre d’expression.

    C’est la pierre de la communication. Elle vous permet de vous affirmer, de
    prendre confiance et de prendre la place qui vous revient dans le monde.
    Elle participe à l’amélioration de vos relations avec l’extérieur.

    Méthode de Calcul :
        Pour l'obtenir, c'est la Somme non réduits des 2 pierres précédentes.
    Args:
        a (int): La valeur de la pierre d’appel non réduite.
        b (int): La valeur de la pierre de personnalité non réduite.
    Returns:
        int: La valeur de la pierre d’expression.
    """
    return a + b


def calcul_touche(a, b, c, d, e) -> int:
    """
    Calcule la pierre de touche.

    C’est la pierre des difficultés. Elle vous offre la lumière et la clarté
    nécessaire pour que vous preniez de bonnes décisions.

    Méthode de Calcul :
        Pour l'avoir, faites la somme non reduites des pierres précédentes à
        l’exception de celle du chemin de vie. Et faites la réduction.
    Args:
        a (int): La valeur de la pierre de base.
        b (int): La valeur de la pierre de sommet.
        c (int): La valeur de la pierre d’appel.
        d (int): La valeur de la pierre de personnalité.
        e (int): La valeur de la pierre d’expression.
    Returns:
        int: La valeur de la pierre de touche.
    """
    return a + b + c + d + e


def calcul_voeux(liste) -> int:
    """
    Calcule la pierre de vœux.

    C’est la pierre qui reflète les émotions de l’être. C’est la pierre de vos
    désirs, et de l’amour qui siège en vous.

    Méthode de Calcul :
        C'est la somme de toutes les premières voyelles des noms et prénoms.
    Args:
        liste (list): Une liste de noms et prénoms.
    Returns:
        int: La valeur de la pierre de vœux.
    """
    somme = 0
    voyelles = 'AEIOUY'
    for word in liste:
        for letter in word:
            if letter.upper() in voyelles:
                somme += u.tableau_de_vie_to_chiffre(letter)
                break
    return somme


def print_equi(base, sommet, vie, appel, perso, expression, touche, voeux):
    print("Vos équivalences de pierres :")
    print(f"\t- Pierre de base est : {u.tab_rock(u.somme_p(base))}")
    print(f"\t- Pierre de sommet est : {u.tab_rock(u.somme_p(sommet))}")
    print(f"\t- Pierre de chemin de vie est : {u.tab_rock(u.somme_p(vie))}")
    print(f"\t- Pierre d'appel est : {u.tab_rock(u.somme_p(appel))}")
    print(f"\t- Pierre de personnalité est : {u.tab_rock(u.somme_p(perso))}")
    print(f"\t- Pierre d'expression est : {u.tab_rock(u.somme_p(expression))}")
    print(f"\t- Pierre de touche est : {u.tab_rock(u.somme_p(touche))}")
    print(f"\t- Pierre de vœux est : {u.tab_rock(u.somme_p(voeux))}")


def main():
    prenoms = input("Entrez vos prénoms 'prenom1 prenom2 ...' : ")
    nomp = input("Entrez le nom du père 'nom' : ")
    nomm = input("Entrez le nom de la mère 'nom' : ")
    date_naissance = input("Entrez votre date de naissance 'JJ.MM.AAAA' : ")
    identity = prenoms.split()
    identity.append(nomp)
    identity.append(nomm)

    # Calculer les différentes pierres
    num_base = calcul_base(identity)
    num_sommet = calcul_sommet(identity)
    num_vie = calcul_chemin_vie(date_naissance)
    num_appel = calcul_appel(identity)
    num_perso = calcul_personnalite(identity)
    num_expression = calcul_expression(num_appel, num_perso)
    num_touche = calcul_touche(
        num_base, num_sommet, num_appel, num_perso, num_expression)
    num_voeux = calcul_voeux(identity)

    # Afficher les résultats
    print_equi(num_base, num_sommet, num_vie, num_appel, num_perso,
               num_expression, num_touche, num_voeux)


if __name__ == "__main__":
    main()
