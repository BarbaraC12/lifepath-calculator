# 1. Obtenir les information necessaire:
#  - Prenoms(s)
#  - Date de naisssaince dd/mm/aaaa
#  - Nom Pere
#  - Nom Mere 
# 2. Orientation pour calculs
# 3. Reduction
# 4. Trouver les pierres correspondante

from p_chemindevie import calcul_chemin_vie

prenoms = input("Entrez vos prenoms au format 'prenom1 prenom2 ...' : ")
# Demander à l'utilisateur d'entrer sa date de naissance
date_naissance = input("Entrez votre date de naissance au format 'JJMMAAAA' : ")
nomp = input("Entrez le nom du pere au format 'nom' : ")
nomm = input("Entrez le nom de la mere au format 'nom' : ")

# Calculer le chemin de vie
chiffre_vie = calcul_chemin_vie(date_naissance)

# Afficher le résultat
print("Votre chiffre chemin de vie est :", chiffre_vie)