def code_miroir(message):
    """
    Applique le chiffrement miroir (aussi appelé Atbash).
    L'alphabet est inversé : 
    A <-> Z
    B <-> Y
    C <-> X
    ...
    M <-> N

    Règles :
    - Les caractères non-alphabétiques (chiffres, ponctuation) restent inchangés.
    - La casse (majuscule/minuscule) est harmonisée en MAJUSCULE.

    Args:
        message (str): Le texte à chiffrer.

    Returns:
        str: Le texte chiffré.

    Example:
        >>> code_miroir("AZ")
        'ZA'
        >>> code_miroir("Hello")
        'SVOOL'
    """
    return NotImplemented



# -------------------------------------------------------------------------
# ESPACE TAMPON POUR LIMITER LES RISQUES DE CONFLIT
# -------------------------------------------------------------------------



def vers_leet_speak(message):
    """
    Transforme le texte en Leet Speak (remplacement par des chiffres).
    
    Dictionnaire de remplacement OBLIGATOIRE :
    E -> 3
    A -> 4
    T -> 7
    I -> 1
    O -> 0
    S -> 5
    
    Règles :
    - Tout doit être mis en majuscules avant la conversion.
    - Les caractères qui ne sont pas dans le dictionnaire restent inchangés.

    Args:
        message (str): Le texte original.

    Returns:
        str: Le texte transformé.

    Example:
        >>> vers_leet_speak("ESTIO")
        '35710'
        >>> vers_leet_speak("Table")
        '74BL3'
    """
    return NotImplemented



# -------------------------------------------------------------------------
# ESPACE TAMPON POUR LIMITER LES RISQUES DE CONFLIT
# -------------------------------------------------------------------------



def depuis_leet_speak(message):
    """
    Retrouve le texte original depuis du Leet Speak.
    Inverse les règles : 3->E, 4->A, 7->T, 1->I, 0->O, 5->S.

    Args:
        message (str): Le texte en Leet Speak.

    Returns:
        str: Le texte lisible (en majuscule).

    Example:
        >>> depuis_leet_speak("35710")
        'ESTIO'
    """
    return NotImplemented



# -------------------------------------------------------------------------
# ESPACE TAMPON POUR LIMITER LES RISQUES DE CONFLIT
# -------------------------------------------------------------------------



def chiffrer_vigenere(message, cle):
    """
    Chiffre avec la méthode de Vigenère (Code César à clé variable).
    """
    message = message.upper()
    cle = cle.replace(" ", "").upper()

    resultat = []
    index_cle = 0
    n = len(cle)

    for char in message:
        if not char.isalpha():
            resultat.append(char)
            continue

        lettre_cle = cle[index_cle % n]
        decalage = ord(lettre_cle) - ord('A')

        # Chiffrement type César
        base = ord('A')
        valeur = (ord(char) - base + decalage) % 26
        resultat.append(chr(base + valeur))

        index_cle += 1

    return "".join(resultat)


# -------------------------------------------------------------------------
# ESPACE TAMPON POUR LIMITER LES RISQUES DE CONFLIT
# -------------------------------------------------------------------------



def dechiffrer_vigenere(message, cle):
    """
    Déchiffre un message Vigenère.
    Même logique que le chiffrement, mais on SOUSTRAIT le décalage au lieu de l'ajouter.

    Args:
        message (str): Le texte chiffré.
        cle (str): La clé utilisée.

    Returns:
        str: Le message en clair.

    Example:
        >>> dechiffrer_vigenere("RLVKD", "CLE")
        'PARIS'
    """
    return NotImplemented