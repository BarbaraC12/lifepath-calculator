import re
from datetime import datetime

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


def tab_rock(number):
    tableau_de_pierre = {
        1: "Quartz rose", 2: "Jaspe rouge ", 3: "Calcédoine",
        4: "Jade", 5: "Émeraude (peut être remplacé par de l’Aventurine)",
        6: "Grenat", 7: "Citrine", 8: "Obsidienne",
        9: "Aigue Marine", 10: "Rhodochrosite", 11: "Cornaline",
        12: "Ambre", 13: "Hématite", 14: "Améthyste",
        15: "Malachite", 16: "Opale", 17: "Turquoise",
        18: "Pierre de Lune", 19: "Topaze", 20: "Lapis Lazuli",
        21: "Tourmaline", 22: "Cristal de Roche", 23: "Azurite",
        24: "Amazonite", 25: "Œil de Tigre", 26: "Pyrite",
        27: "Fluorine", 28: "Perle", 29: "Sodalite", 30: "Quartz Fumé",
        31: "Souffre (peut être remplacé par de la Pierre de Lune)",
        32: "Mercure (peut être remplacé par de l’Agate Mokaïte)",
        33: "Sel (peut être remplacé par du Quartz Toumaliné)",
    }
    return tableau_de_pierre.get(number)


def somme_p(nombre):
    while nombre >= 33:
        nombre = sum(int(chiffre) for chiffre in str(nombre))
    return nombre


def year_to_four_digit(year):
    if len(year) == 2:
        current_year = datetime.now().year
        if year <= str(current_year)[2:]:
            prefix = str(current_year)[:2]
        else:
            prefix = "19"
        year = f"{prefix}{year}"
    return year


def split_date(date_str):
    date_formats = [
        r'(\d{2})[./\s](\d{2})[./\s](\d{4})',  # DD/MM/YYYY, DD.MM.YYYY, DD MM YYYY
        r'(\d{2})(\d{2})(\d{4})',              # DDMMYYYY
        r'(\d{2})[./\s](\d{2})[./\s](\d{2})',  # DD/MM/YY, DD.MM.YY, DD MM YY
        r'(\d{2})(\d{2})(\d{2})',              # DDMMYY
    ]
    for regex in date_formats:
        match = re.match(regex, date_str)
        if match:
            day, month, year = match.groups()
            year = year_to_four_digit(year)
            return int(day), int(month), int(year)
    return None, None, None
