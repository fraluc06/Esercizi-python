"""
Challenge 03: Configurazione del personaggio
Sistema di configurazione per un personaggio Eroe in un gioco RPG
"""

# Definizione delle classi disponibili (contenitore immutabile: lista di tuple)
CLASSI_DISPONIBILI = [
    ("Guerriero", 120),
    ("Mago", 80),
    ("Arciere", 100),
    ("Paladino", 110)
]


def mostra_storia():
    """Mostra la storia introduttiva del gioco"""
    print("\n" + "=" * 60)
    print("STORIA")
    print("=" * 60)
    print("Benvenuto nel regno di Eldoria!")
    print("Una terra antica minacciata da forze oscure...")
    print("Sei stato scelto per diventare l'Eroe che salverà il regno.")
    print("Ma prima, devi prepararti per l'avventura che ti aspetta.")
    print("=" * 60)


def valida_nome(nome):
    """
    Valida il nome del personaggio
    Requisiti: lunghezza tra 3 e 15 caratteri
    """
    return 3 <= len(nome) <= 15


def mostra_classi():
    """Mostra le classi disponibili"""
    print("\nClassi disponibili:")
    for i, (nome_classe, hp) in enumerate(CLASSI_DISPONIBILI, 1):
        print(f"{i}. {nome_classe} (HP: {hp})")

def scegli_classe():
    """
    Permette di scegliere una classe tramite indice
    Ritorna una tupla (nome_classe, hp) o None se la scelta non è valida
    """
    mostra_classi()

    try:
        scelta = int(input("\nSeleziona il numero della classe: "))

        # Itera sulle classi disponibili per validare e ottenere la classe scelta
        for i, classe in enumerate(CLASSI_DISPONIBILI, 1):
            if i == scelta:
                return classe

        print("❌ Scelta non valida!")
        return None

    except ValueError:
        print("❌ Inserisci un numero valido!")
        return None


def fase_configurazione(personaggio):
    """
    Fase di configurazione del personaggio
    Usa un ciclo while True con break solo quando tutti i dati sono validati
    """
    print("\n" + "=" * 60)
    print("CONFIGURAZIONE PERSONAGGIO")
    print("=" * 60)

    # Ciclo di configurazione
    while True:
        print("\n--- Menu Configurazione ---")
        print("1. Scegli Nome")
        print("2. Scegli Classe")
        print("3. Completa Configurazione")

        comando = input("\nInserisci il numero dell'opzione: ").strip()

        # Gestione logica/comandi interni con match/case
        match comando:
            case "1":
                nome = input("\nInserisci il nome del tuo eroe (3-15 caratteri): ").strip()

                if valida_nome(nome):
                    personaggio["nome"] = nome
                    print(f"✓ Nome impostato: {nome}")
                else:
                    print("❌ Nome non valido! Deve essere tra 3 e 15 caratteri.")

            case "2":
                classe_scelta = scegli_classe()

                if classe_scelta:
                    nome_classe, hp = classe_scelta
                    personaggio["classe"] = nome_classe
                    personaggio["hp"] = hp
                    print(f"✓ Classe impostata: {nome_classe} (HP: {hp})")

            case "3":
                # Verifica che tutti i dati obbligatori siano presenti
                if "nome" not in personaggio:
                    print("❌ Devi prima scegliere un nome!")
                elif "classe" not in personaggio:
                    print("❌ Devi prima scegliere una classe!")
                else:
                    print("\n✓ Configurazione completata!")
                    print(f"Eroe: {personaggio['nome']}")
                    print(f"Classe: {personaggio['classe']}")
                    print(f"HP: {personaggio['hp']}")
                    break  # Uscita dal ciclo di configurazione

            case _:
                print("❌ Comando non riconosciuto. Riprova.")


def main():
    """
    Ciclo globale del gioco (Main Loop)
    Utilizza match/case per gestire le fasi principali
    """
    # Inizializzazione stato del personaggio (Dizionario)
    personaggio = {}

    print("🎮 BENVENUTO NEL GIOCO RPG 🎮")

    # Ciclo principale del gioco
    while True:
        print("\n" + "=" * 60)
        print("MENU PRINCIPALE")
        print("=" * 60)
        print("1. Storia")
        print("2. Configurazione Personaggio")
        print("3. Termina")

        comando_principale = input("\nInserisci il numero dell'opzione: ").strip()

        # Gestione fasi principali con structural pattern matching
        match comando_principale:
            case "1":
                mostra_storia()

            case "2":
                fase_configurazione(personaggio)

            case "3":
                print("\n👋 Grazie per aver giocato! Arrivederci!")
                break

            case _:
                print("❌ Comando non riconosciuto. Riprova.")


if __name__ == "__main__":
    main()
