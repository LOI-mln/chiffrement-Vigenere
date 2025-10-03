import re
from collections import Counter

def kasiski(texte_chiffre, taille_ngramme_min=3, taille_ngramme_max=5, longueur_cle_max=20):

    texte_nettoye = re.sub(r'[^A-Z]', '', texte_chiffre.upper())
    if len(texte_nettoye) < 20:
        return []

    votes_diviseurs = Counter()

    taille_ngramme = taille_ngramme_min
    while taille_ngramme <= taille_ngramme_max:
        positions_ngrammes = {}
        indice = 0
        while indice <= len(texte_nettoye) - taille_ngramme:
            ngramme = texte_nettoye[indice:indice + taille_ngramme]
            if ngramme in positions_ngrammes:
                positions_ngrammes[ngramme].append(indice)
            else:
                positions_ngrammes[ngramme] = [indice]
            indice += 1

        liste_distances = []
        for positions in positions_ngrammes.values():
            if len(positions) > 1:
                a = 0
                while a < len(positions):
                    b = a + 1
                    while b < len(positions):
                        distance = positions[b] - positions[a]
                        if distance > 1:
                            liste_distances.append(distance)
                        b += 1
                    a += 1

        for distance in liste_distances:
            diviseurs = []
            borne = distance if distance < longueur_cle_max else longueur_cle_max
            diviseur = 2
            while diviseur <= borne:
                if distance % diviseur == 0:
                    diviseurs.append(diviseur)
                diviseur += 1

            if len(diviseurs) > 0:
                poids = 1.0 / len(diviseurs)
                for d in diviseurs:
                    votes_diviseurs[d] += poids

        taille_ngramme += 1

    if not votes_diviseurs:
        return []

    longueurs_triees = sorted(votes_diviseurs.items(), key=lambda x: (-x[1], x[0]))

    if len(longueurs_triees) > 1 and longueurs_triees[0][0] == 2:
        if longueurs_triees[1][0] > 2 and (longueurs_triees[0][1] - longueurs_triees[1][1]) <= 0.5:
            longueurs_triees = [longueurs_triees[1], longueurs_triees[0]] + longueurs_triees[2:]

    return [longueur for longueur, score in longueurs_triees]

if __name__ == "__main__":
    nom_fichier = input("Entrez le nom du fichier contenant le texte chiffré : ")

    try:
        with open(nom_fichier, "r", encoding="utf-8") as f:
            texte_chiffre = f.read()
    except FileNotFoundError:
        print("Erreur : fichier introuvable.")
        exit()
    longueurs_probables = kasiski(
        texte_chiffre,
        taille_ngramme_min=3,
        taille_ngramme_max=5,
        longueur_cle_max=20
    )
    if longueurs_probables:
        print("Tailles probables de la clé (par ordre de probabilité) :", longueurs_probables)
    else:
        print("Impossible d'estimer la longueur de la clé (texte trop court ou peu de répétitions).")
