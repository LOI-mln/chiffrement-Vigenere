def chiffrement_vigenere(texte_clair, clef):
    texte_chiffre = ""
    longueur_clef = len(clef)
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    texte_clair = texte_clair.upper()
    clef = clef.upper()

    for i, lettre in enumerate(texte_clair):
        if lettre in alphabet:
            position_lettre = alphabet.index(lettre)
            position_clef = alphabet.index(clef[i % longueur_clef])
            position_chiffree = (position_lettre + position_clef) % len(alphabet)
            lettre_chiffree = alphabet[position_chiffree]
            texte_chiffre += lettre_chiffree
        else:
            texte_chiffre += lettre  

    return texte_chiffre

if __name__ == "__main__":
    texte_clair = input("Entrez le texte clair : ")
    clef = input("Entrez la clé : ")
    texte_chiffre = chiffrement_vigenere(texte_clair, clef)
    print("Texte chiffré :", texte_chiffre)