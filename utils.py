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

def somme_chiffres(nombre):
    while nombre >= 10:
        nombre = sum(int(chiffre) for chiffre in str(nombre))
    return nombre

