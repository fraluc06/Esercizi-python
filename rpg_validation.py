# -*- coding: utf-8 -*-
# attività di gruppo: il test della sentinella
# obiettivo: usare funzioni, if/elif/else e metodi stringa per validare un input.

# ==============================================================================
# Definizione della Funzione di Verifica
# ==============================================================================



def verifica_nome():
    """
    Funzione che richiede un nome all'utente ed esegue una singola verifica.
    Restituisce il nome pulito se valido, altrimenti None.
    """
    nome_input = input("sentinella: dichiara il tuo nome (un solo tentativo): ")

    return verify_str(nome_input)


def verify_str(nome_input):
    # Tappa 1: Pulizia dell'Input (Metodi Stringa)
    # Usiamo .strip() per rimuovere spazi bianchi all'inizio e alla fine.
    nome_pulito = nome_input.strip()
    # Tappa 2: Validazione di Sicurezza (if/elif/else)
    # Regola 1: Controllo se il nome è vuoto
    # Usiamo 'not' per verificare se la stringa pulita è vuota (False).
    if not nome_pulito:
        return None
    # Regola 2: Controllo della Lunghezza
    # Il nome deve essere tra 3 e 15 caratteri (inclusi).
    if not (3 <= len(nome_pulito) <= 15):
        return None
    # Regola 3: Controllo Alfabetico (deve contenere almeno un numero)
    # Usiamo una 'generator expression' con .isdigit() e any() per verificare
    # rapidamente se ALMENO UN carattere è una cifra.
    # for i in range(len(nome_pulito)):
    #     carattere = nome_pulito[i]


    has_digit = False
    for carattere in nome_pulito:
        if carattere.isdigit():
            has_digit = True
            break
    
    # Regola 4: Parola Chiave Proibita ("lord") - solo se non ci sono cifre
    # Convertiamo la stringa in minuscolo con .lower() per rendere il controllo case-insensitive.
    if not has_digit and "lord" in nome_pulito.lower():
        return None
    
    if not has_digit:
        return None
    # Successo!
    # Se tutte le condizioni sopra sono False, il codice entra nell'else.
    else:
        # Tappa 3: Successo!
        print(f"sentinella: accesso garantito, {nome_pulito}. benvenuto nella fortezza!")
        return nome_pulito  # Restituisce il nome valido


# ==============================================================================
# Blocco Principale del Programma (Punto di Inizio)
# ==============================================================================

def test_verify_str():
    test_cases = [
        ('lord byron', None),
        ('Lord Byron!!!', None),
        ('Lordura', None),
        ('Lordura123', 'Lordura123',),
        ('', None),
        ('MySecretPassword1!', None),
        ('MySecretPwd1!', 'MySecretPwd1!'),
        ('MySuperDuperSecretPassword1!1!!!!!!', None),
    ]
    for in_str, expected in test_cases:
        if verify_str(in_str)!=expected:
            print(f'check on {in_str} failed, expected: {expected}')
        assert verify_str(in_str) == expected

if __name__ == "__main__":

    test_verify_str()
    # print("\n--- inizio esame sentinella ---\n")
    # #
    # # # Chiamiamo la funzione che esegue la verifica
    # risultato = verifica_nome()
    # #
    # # # Uso di if/else per reagire al risultato della funzione
    # # # Se risultato è diverso da None (cioè, True), l'eroe procede.
    # if risultato:
    # #     # Codice eseguito in caso di successo
    #     print(f"\n[codice di successo: l'eroe {risultato} inizia l'avventura!]")
    # #
    # else:
    # #     # Codice eseguito in caso di fallimento
    #     print("\n[codice di fallimento: il personaggio non è stato creato. riavviare per un nuovo tentativo.]")