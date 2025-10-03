# Documentation du projet – Vigenère & Kasiski (Python)

Ce document regroupe en **un seul fichier** : un **README** synthétique pour l’utilisation et la présentation du dépôt, puis le **compte rendu** détaillé contenant rappels théoriques, jeux d’essai et conclusions.

---

## README (synthèse du projet)

### Vigenère & Kasiski – Mini-projet Python

Ensemble de scripts pour chiffrer/déchiffrer un texte avec le chiffre de **Vigenère** et estimer la **longueur de clé** avec une ébauche de la **méthode de Kasiski**.

> Pour l’analyse détaillée et les résultats, voir la section **“Compte rendu”** ci‑dessous.

### Contenu du dépôt

```
.
├── chiffrement_vigenere.py        # Chiffrement interactif (A–Z, le reste inchangé)
├── dechiffrement_vigenere.py      # Déchiffrement interactif
├── kasiski.py                     # Estimation de longueur de clé (ébauche)
├── texte_clair.txt                # Exemple de texte clair
├── texte_chiffre.txt              # Exemple de texte chiffré
└── README.md                      # README du dépôt (si séparé)
```

### Prérequis

- Python 3.8+
- Windows / macOS / Linux

Les scripts opèrent sur l’alphabet **A–Z** (majuscules). Les caractères non A–Z (espaces, ponctuation, accents, chiffres) sont laissés inchangés.

### Jeux d’essai (extraits)

**Test A – Phrase courte**  
- Clé : `CLE`  
- Clair : `BONJOUR TOUT LE MONDE … SANS ACCENTS.`  
- Chiffré :
```
DZRLZYT XQFX WI XSPOI NIET GDX FR EIUE FF ESMHQVGXIPE FP XTKGYITP UFV FR LPRSEDPX DMOAPG WCYW LGEPRVD.
```
- Déchiffrement → texte d’origine (OK)

**Test B – Fichier `texte_clair.txt`**  
- Clé : `CLEF`  
- Début clair : `L’INFORMATIQUE EST UNE DISCIPLINE VASTE …`  
- Début chiffré : `N’MSHZVRCEMVWP JUE ZPP IKDGNRWMSG …`  
- Vérification : déchiffrement(`chiffré`, `CLEF`) = clair (OK)

**Test C – Kasiski sur `texte_chiffre.txt`**  
- Résultat : longueurs candidates ≈ `[2, 3, 5, 4, 6, 7, 10, 9]`

### Détails d’implémentation

- Alphabet : `A=0 … Z=25` ; calculs modulo 26.  
- Chiffrement : `c_i = (t_i + k_{i mod m}) mod 26`  
- Déchiffrement : `t_i = (c_i − k_{i mod m}) mod 26`  
- Complexité : O(n) en temps, O(1) mémoire auxiliaire (hors E/S).  
- Entrées à éviter : clé vide ; clé contenant des caractères hors A–Z.

### Auteurs et licence

- Auteur : à compléter  
- Licence : à définir (ex. MIT)

---

## Compte rendu – Chiffrement/déchiffrement de Vigenère & estimation de clé (méthode de Kasiski)

**Auteur :** —**Date :** 03/10/2025**Contexte :** BUT Informatique – cryptographie

### 1) Objectifs de l’exercice

- Implémenter le chiffrement et le déchiffrement du chiffre de **Vigenère**.
- Proposer une première approche d’**attaque** par **méthode de Kasiski** pour **estimer la longueur de la clé** à partir d’un texte chiffré.
- Valider l’implémentation au moyen de **jeux d’essai** (tests) et commenter les **limites** et **améliorations** possibles.

### 2) Rappel théorique (très bref)

- **Vigenère** : chiffrement polyalphabétique. Pour une clé *K* = k₀…kₘ₋₁ et un texte *T* = t₀…tₙ₋₁ (lettres A–Z), on chiffre par :  cᵢ = (tᵢ + k_{i mod m}) mod 26.  Le déchiffrement inverse :  tᵢ = (cᵢ − k_{i mod m}) mod 26.
- **Kasiski** : on repère des **n-grammes répétés** dans le texte chiffré et on étudie les **distances** entre répétitions ; les **diviseurs communs** de ces distances suggèrent la **longueur de la clé**.

### 3) Organisation du dépôt & fichiers livrés

- `chiffrement_vigenere.py` : fonction `chiffrement_vigenere(texte_clair, clef)` et exécutable interactif (saisie au clavier).
- `dechiffrement_vigenere.py` : fonction symétrique `dechiffrement_vigenere(texte_chiffre, clef)` et exécutable interactif.
- `kasiski.py` : ébauche d’implémentation de la méthode de Kasiski, avec lecture d’un fichier et affichage des tailles de clé probables.
- Fichiers texte fournis :  `texte_clair.txt` (≈ 3548 lettres A–Z utiles) et `texte_chiffre.txt` (≈ 3548 lettres A–Z utiles sur 4416 caractères au total).

**Convention d’implémentation (chiffrement/déchiffrement)**

- Alphabet **A…Z** uniquement.
- Les **caractères non A–Z** (espaces, ponctuation, **accents**, chiffres) sont **laissés inchangés**.
- La **clé doit être non vide** et **composée de lettres A–Z** (en dehors de ce domaine, une erreur d’index peut survenir).

**Complexité**Chaque transformation parcourt linéairement le texte : **O(n)** temps, **O(1)** mémoire auxiliaire.

### 4) Mode d’emploi (exécutable)

- Chiffrement :
  1. Lancer : `python3 chiffrement_vigenere.py`
  2. Saisir le **texte clair**, puis la **clé**.
  3. Le programme affiche : `Texte chiffré : …`
- Déchiffrement :
  1. Lancer : `python3 dechiffrement_vigenere.py`
  2. Saisir le **texte chiffré**, puis la **clé**.
  3. Le programme affiche : `Texte déchiffré : …`
- Estimation (Kasiski) :
  1. Lancer : `python3 kasiski.py`
  2. Le script charge un texte chiffré et affiche une **liste ordonnée de longueurs de clé probables**.

> **Remarque** : dans l’état actuel, `kasiski.py` est une **ébauche** (section Améliorations) ; l’estimation reste indicative.

### 5) Jeux d’essai & résultats

**Test 1 – Phrase courte de validation**

- **Texte clair** (extrait) : `BONJOUR TOUT LE MONDE … SANS ACCENTS.`
- **Clé** : `CLE`
- **Texte chiffré** obtenu :

```
DZRLZYT XQFX WI XSPOI NIET GDX FR EIUE FF ESMHQVGXIPE FP XTKGYITP UFV FR LPRSEDPX DMOAPG WCYW LGEPRVD.
```

- **Déchiffrement** avec la même clé → **identique à l’original** (OK).

**Test 2 – Fichier `texte_clair.txt` avec clé connue**

- **Clé** : `CLEF` (longueur 4)
- **Statistiques** :
  - Caractères totaux (extrait utilisé pour affichage) : 300
  - **Lettres A–Z chiffrées** : 241
- **Début du texte clair** :

```
L’INFORMATIQUE EST UNE DISCIPLINE VASTE ET PASSIONNANTE QUI A PRO…
```

- **Début du texte chiffré** (avec `CLEF`) :

```
N’MSHZVRCEMVWP JUE ZPP IKDGNRWMSG ZFUEI GE UCDWNQYRFPEI SFM C …
```

- **Vérification** : déchiffrement(`texte_chiffré`, `CLEF`) = **texte clair** (OK) ; **toutes les ponctuations/accents sont préservés**.

**Test 3 – Estimation de la longueur de clé (Kasiski)**

- **Entrée** : `texte_chiffre.txt` fourni (4416 caractères dont ~3548 lettres A–Z).
- **Sortie (top 8 longueurs candidates)** :

```
[2, 3, 5, 4, 6, 7, 10, 9]
```

- **Interprétation** : la méthode suggère de **petites longueurs** (2–7) ; en pratique, on teste ces valeurs (par ex. 4, 5, 6) puis on poursuit par une **analyse fréquentielle par colonne** pour affiner la clé lettre par lettre.
- **Limite constatée** : la présence d’accents/ponctuation (bien que non chiffrés) et la richesse du corpus rendent les **répétitions** moins franches ; un **prétraitement** (normalisation ASCII) et un **vote pondéré** des diviseurs améliorent la robustesse.

### 6) Points de qualité & cas limites

- **Clé vide** → division modulo par 0 : **à interdire** (à valider côté IHM).
- **Clé avec caractères non A–Z** → l’indexation de l’alphabet échoue : **contrôle d’entrée** recommandé.
- **Accents et lettres hors A–Z** → non chiffrés (choix assumé) ; pour une attaque efficace, prévoir une **normalisation** (supprimer accents et passer en A–Z) en **copie de travail**, sans altérer l’affichage utilisateur.

### 7) Améliorations proposées

1. **kasiski.py complet** :
   - Recherche de tous les **n-grammes** (n=3..5), prise en compte de **toutes les paires** d’occurrences et **pondération** des votes par le nombre d’occurrences.
   - **Filtrage** pour éviter le biais systématique vers 2 (fréquent).
   - Ajout d’un **deuxième critère** (Indice de coïncidence par colonne) pour choisir la **meilleure longueur** parmi les candidates.
2. **Interface fichiers** : versions de `chiffrement_*.py` et `dechiffrement_*.py` capables de **lire/écrire** des fichiers pour manipuler de longs textes.
3. **Normalisation optionnelle** : bascule "affichage fidèle" / "analyse A–Z".
4. **Jeu de tests automatisés** (pytest) : cas standards + cas d’erreur (clé vide, caractères hors A–Z, etc.).

### 8) Conclusion

L’implémentation de base du chiffre de Vigenère **fonctionne** et passe les **tests de validation** (phrase courte et long texte). L’ébauche de la méthode de Kasiski permet déjà de **réduire l’espace de recherche** pour la longueur de clé, mais gagnerait à être **complétée** (pondération, indice de coïncidence, normalisation). Ces améliorations constitueraient l’étape suivante d’une **attaque pratique** du chiffre.

### 9) Annexes (extraits et mesures)

- `texte_clair.txt` – premières ~300 caractères :

> L’INFORMATIQUE EST UNE DISCIPLINE VASTE ET PASSIONNANTE QUI A …

- `texte_chiffre.txt` – premiers ~300 caractères :

> N’BETBTUTKWDWM VGG CGV QKAVZDYKVX JNUBX SG XTJGVQVGRBGG JLW C …

- **Compteurs** :  `len(texte_chiffre.txt)` = 4416 caractères ; lettres A–Z utiles ≈ 3548 (identique au clair).

---

**Fin du document**

