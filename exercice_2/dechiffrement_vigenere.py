def dechiffrement_vigenere(texte_chiffre, clef):
    texte_clair = ""
    longueur_clef = len(clef)
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    texte_chiffre = texte_chiffre.upper()
    clef = clef.upper()

    for i, lettre in enumerate(texte_chiffre):
        if lettre in alphabet:
            position_lettre = alphabet.index(lettre)
            position_clef = alphabet.index(clef[i % longueur_clef])
            position_claire = (position_lettre - position_clef) % len(alphabet)
            lettre_claire = alphabet[position_claire]
            texte_clair += lettre_claire
        else:
            texte_clair += lettre  

    return texte_clair

if __name__ == "__main__":
    texte_chiffre = input("Entrez le texte chiffré : ")
    clef = input("Entrez la clé : ")
    texte_clair = dechiffrement_vigenere(texte_chiffre, clef)
    print("Texte déchiffré :", texte_clair)