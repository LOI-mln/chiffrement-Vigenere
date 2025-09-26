import re
from collections import Counter

def kasiski(texte_chiffre, taille_ngramme=3, longueur_cle_max=20):
    """
    Estime la longueur probable de la clé d'un Vigenère avec la méthode de Kasiski.
    - Recherche les n-grammes répétés et calcule toutes les distances entre leurs occurrences.
    - Vote pour les diviseurs (2..longueur_cle_max) de ces distances.
    - Renvoie UNE seule longueur (la plus probable).
    """
    texte_nettoye = re.sub(r'[^A-Z]', '', texte_chiffre.upper())
    if len(texte_nettoye) < 20:
        return None

    occurrences_sequences = {}
    i = 0
    while i <= len(texte_nettoye) - taille_ngramme:
        ngramme = texte_nettoye[i:i + taille_ngramme]
        if ngramme in occurrences_sequences:
            occurrences_sequences[ngramme].append(i)
        else:
            occurrences_sequences[ngramme] = [i]
        i += 1

    liste_distances = []
    for positions in occurrences_sequences.values():
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

    liste_diviseurs = []
    for distance in liste_distances:
        borne_superieure = distance if distance < longueur_cle_max else longueur_cle_max
        diviseur = 2
        while diviseur <= borne_superieure:
            if distance % diviseur == 0:
                liste_diviseurs.append(diviseur)
            diviseur += 1

    if not liste_diviseurs:
        return None 

    compteur_diviseurs = Counter(liste_diviseurs)

    meilleur_diviseur = None
    meilleur_score = -1
    for longueur, score in compteur_diviseurs.items():
        if score > meilleur_score or (score == meilleur_score and longueur < meilleur_diviseur):
            meilleur_diviseur = longueur
            meilleur_score = score

    return meilleur_diviseur

if __name__ == "__main__":
    texte_chiffre = input("Entrez le texte chiffré : ")
    longueur = kasiski(texte_chiffre, taille_ngramme=3, longueur_cle_max=20)
    if longueur:
        print("Longueur probable de la clé :", longueur)
    else:
        print("Pas assez de répétitions pour estimer la longueur de clé.")
