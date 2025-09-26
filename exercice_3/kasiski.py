import re
from collections import Counter

def kasiski(texte_chiffre, taille_ngramme_min=3, taille_ngramme_max=5, longueur_cle_max=20):
    """
    Estime UNE seule longueur probable de la clé utilisée pour le chiffrement Vigenère
    grâce à la méthode de Kasiski.
    
    Améliorations incluses :
      - On teste plusieurs tailles d’ngrams (3 à 5 par défaut).
      - Chaque distance trouvée distribue son vote sur ses diviseurs (pondération).
      - Si la longueur 2 est à peine meilleure qu’une autre longueur > 2,
        on choisit plutôt l’autre (évite de tomber toujours sur 2).
    """

    texte_nettoye = re.sub(r'[^A-Z]', '', texte_chiffre.upper())
    if len(texte_nettoye) < 20:
        return None 

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
        return None  

    meilleure_longueur = None
    meilleur_score = -1.0
    seconde_longueur = None
    second_score = -1.0

    for longueur, score in votes_diviseurs.items():
        if (score > meilleur_score) or (score == meilleur_score and (meilleure_longueur is None or longueur < meilleure_longueur)):
            seconde_longueur, second_score = meilleure_longueur, meilleur_score
            meilleure_longueur, meilleur_score = longueur, score
        elif (score > second_score) or (score == second_score and (seconde_longueur is None or longueur < seconde_longueur)):
            seconde_longueur, second_score = longueur, score


    if meilleure_longueur == 2 and seconde_longueur is not None:
        if (seconde_longueur > 2) and (meilleur_score - second_score) <= 0.5:
            return seconde_longueur

    return meilleure_longueur

if __name__ == "__main__":
    nom_fichier = input("Entrez le nom du fichier contenant le texte chiffré : ")

    try:
        with open(nom_fichier, "r", encoding="utf-8") as f:
            texte_chiffre = f.read()
    except FileNotFoundError:
        print("Erreur : fichier introuvable.")
        exit()
    longueur_probable = kasiski(
        texte_chiffre,
        taille_ngramme_min=3,
        taille_ngramme_max=5,
        longueur_cle_max=20
    )
    if longueur_probable:
        print("Longueur probable de la clé :", longueur_probable)
    else:
        print("Impossible d'estimer la longueur de la clé (texte trop court ou peu de répétitions).")
