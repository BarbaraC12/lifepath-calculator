def tableau_de_vie_to_chiffre(lettre):
    tableau_de_vie = {
        'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5,
        'F': 6, 'G': 7, 'H': 8, 'I': 9,
        'J': 1, 'K': 2, 'L': 3, 'M': 4, 'N': 5,
        'O': 6, 'P': 7, 'Q': 8, 'R': 9,
        'S': 1, 'T': 2, 'U': 3, 'V': 4, 'W': 5,
        'X': 6, 'Y': 7, 'Z': 8,
    }
    
    return tableau_de_vie.get(lettre.upper(), 0)  

def tableau_chiffre_to_pierre(number):
    tableau_de_pierre = {
        1 : "Quartz rose", 2 : "Jaspe rouge ", 3 : "Calcédoine",
        4 : "Jade", 5 : "Émeraude (peut être remplacé par de l’Aventurine)",
        6 : "Grenat", 7 : "Citrine", 8 : "Obsidienne",
        9 : "Aigue Marine", 10: "Rhodochrosite", 11 : "Cornaline",
        12 : "Ambre", 13 : "Hématite", 14 : "Améthyste",
        15 : "Malachite", 16 : "Opale", 17 : "Turquoise",
        18 : "Pierre de Lune", 19 : "Topaze", 20 : "Lapis Lazuli",
        21 : "Tourmaline", 22 : "Cristal de Roche", 23 : "Azurite",
        24 : "Amazonite", 25 : "Œil de Tigre", 26 : "Pyrite",
        27 : "Fluorine", 28 : "Perle", 29 : "Sodalite", 30 : "Quartz Fumé",
        31 : "Souffre (peut être remplacé par de la Pierre de Lune)",
        32 : "Mercure (peut être remplacé par de l’Agate Mokaïte)",
        33 : "Sel (peut être remplacé par du Quartz Toumaliné)",
    }
    return tableau_de_pierre.get(number)

def somme_chiffres(nombre):
    while nombre >= 33:
        nombre = sum(int(chiffre) for chiffre in str(nombre))
    return nombre

