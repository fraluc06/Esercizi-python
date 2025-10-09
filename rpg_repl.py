import time
import sys
from io import StringIO

# --- Variabili Globali del Personaggio ---
character_data = {
    "name": None,
    "age": None,
    "role": None,
    "health": None,
    "mana": None
}


def print_with_delay(text, delay=0.02):
    """Stampa il testo carattere per carattere con un leggero ritardo."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    # Non stampiamo il newline qui, lo facciamo separatamente per aggiungere il suono.


def show_intro():
    """Mostra l'introduzione narrativa."""
    story = [
        "Nelle antiche terre di Pyldoria, dove il codice è legge...",
        "I regni digitali sono sull'orlo del caos e l'oscurità del 'Syntax Error' incombe...",
        "Le leggende parlano di un Eroe che plasmerà il destino di tutti...",
        "Ma prima, l'Eroe deve dichiarare la propria esistenza al Cronista Antico..."
    ]

    for line in story:
        print_with_delay(line)
        print()  # Aggiunge il newline dopo la riga con delay
        time.sleep(0.3)

    print_with_delay("\nBenvenuto, avventuriero. Il tuo viaggio inizia con l'auto-dichiarazione.")
    print()
    time.sleep(0.3)
    print_with_delay("Dovrai definire il tuo essere al Cronista che registra i Destini.")
    print()
    time.sleep(0.3)
    print_with_delay(
        "Definisci il tuo nome (str), la tua età (int), il tuo ruolo (str), i tuoi HP (int) e il tuo Mana (float).")
    print()
    time.sleep(0.3)
    print_with_delay("Il Cronista è molto esigente e accetta solo la sintassi Python corretta: 'variabile = valore'.")
    print()
    time.sleep(0.3)
    print_with_delay("Quando ti sentirai pronto, digita: 'completa la storia'.")
    print()
    time.sleep(0.3)


def update_character_data(variables):
    """
    Analizza lo stato delle variabili globali dopo l'esecuzione del codice
    e aggiorna lo stato del personaggio, controllando i tipi.
    """
    for key in character_data:
        if key in variables:
            value = variables[key]
            current_type = type(value)

            # Controllo del tipo basato sulla variabile
            is_valid = False
            if key in ("name", "role"):
                is_valid = isinstance(value, str)
            elif key in ("age", "health"):
                is_valid = isinstance(value, int)
            elif key == "mana":
                is_valid = isinstance(value, (int, float))  # Mana può essere float o int

            if not is_valid:
                print_with_delay(
                    f"Il Cronista aggrotta la fronte: La variabile '{key}' ha un tipo non idoneo ({current_type.__name__}). Ricorda: nome e ruolo devono essere stringhe (tra virgolette!), età e HP interi (int), e il Mana può essere decimale (float).")
                print()
                continue

            # Se è valido, aggiorna e notifica
            if character_data[key] != value:
                character_data[key] = value
                print_with_delay(f"Il Cronista registra la variabile '{key}': {value} ({current_type.__name__}).")
                print()


def launch_repl():
    """Lancia l'interfaccia REPL personalizzata."""
    print_with_delay("\nIl Cronista ascolta... Parla con saggezza.")
    print()

    # Inizializza l'ambiente di esecuzione con le variabili di stato attuali
    execution_scope = character_data.copy()

    while True:
        try:
            input_line = input("Cronista> ")
        except EOFError:
            print("\nChiusura forzata.")
            break

        input_line = input_line.strip()

        if not input_line:
            continue

        if input_line.lower() == "completa la storia":
            missing = [k for k, v in character_data.items() if v is None]

            if missing:
                print_with_delay(
                    f"\nIl Cronista corruga la fronte. 'Non hai ancora completato la tua storia. Mancano: {', '.join(missing)}'.")
                print()
                continue

            print_with_delay("\nIl Cronista annuisce solennemente e incide le parole finali...")
            print()
            print_with_delay("----------------------")
            print()
            print_with_delay(f"Nome: {character_data['name']} (str)")
            print()
            print_with_delay(f"Età: {character_data['age']} (int)")
            print()
            print_with_delay(f"Ruolo: {character_data['role']} (str)")
            print()
            print_with_delay(f"Salute (HP): {character_data['health']} (int)")
            print()
            print_with_delay(f"Mana: {character_data['mana']} (float)")
            print()
            print_with_delay("----------------------")
            print()

            # --- AGGIUNTA DEL SUONO TRAMITE BEL CHARACTER (\a) ---
            final_message = f"Vai avanti, {character_data['name']}, il/la {character_data['role']} di {character_data['age']} anni. Il tuo destino è scritto. Buona fortuna!\a"
            print_with_delay(final_message)
            print()
            # ----------------------------------------------------

            break

        try:
            # 1. Analisi preliminare: se c'è un '=', esegui come assegnazione
            if '=' in input_line:
                exec(input_line, execution_scope)
                update_character_data(execution_scope)

            else:
                # 2. Se non è un'assegnazione, valuta come espressione
                old_stdout = sys.stdout
                redirected_output = StringIO()
                sys.stdout = redirected_output

                try:
                    eval_result = eval(input_line, execution_scope)
                    if eval_result is not None:
                        # Stampa esplicita del risultato di un'espressione
                        print(eval_result)

                except NameError as e:
                    print_with_delay(f"Il Cronista non trova nulla. Errore: {e}")
                except Exception as e:
                    print_with_delay(f"Il Cronista è perplesso. Errore inaspettato: {e}")

                finally:
                    sys.stdout = old_stdout
                    output = redirected_output.getvalue().strip()
                    if output:
                        print_with_delay(f"Il Cronista mormora: {output}")
                        print()

        except SyntaxError:
            print_with_delay(
                "Il Cronista è confuso. 'La sintassi è errata! Riprova con la sintassi Python standard (es. nome = \"Gimli\")'.")
            print()
        except Exception as e:
            print_with_delay(f"Il Cronista guarda il codice con sospetto. Errore di esecuzione: {e}")
            print()


if __name__ == "__main__":
    show_intro()
    launch_repl()