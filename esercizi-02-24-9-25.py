# Esercizi per casa - 24 Settembre 2025
# Tipi di Dati, Input, Stampa, Conversioni ed Espressioni

# Esercizio 1: Somma e Prodotto
def esercizio_1():
    print("=== Esercizio 1: Somma e Prodotto ===")
    primo_numero = int(input("Inserisci il primo numero intero: "))
    secondo_numero = int(input("Inserisci il secondo numero intero: "))

    somma = primo_numero + secondo_numero
    prodotto = primo_numero * secondo_numero

    print(f"Somma: {somma} (tipo: {type(somma)})")
    print(f"Prodotto: {prodotto} (tipo: {type(prodotto)})")

# Esercizio 2: Divisione normale, divisione intera e resto
def esercizio_2():
    print("\n=== Esercizio 2: Divisione normale, divisione intera e resto ===")
    primo_numero = int(input("Inserisci un numero intero: "))
    secondo_numero = int(input("Inserisci un numero intero: "))

    if secondo_numero == 0:
        print("Errore: divisione per zero non permessa!")
        return

    divisione_normale = primo_numero / secondo_numero
    divisione_intera = primo_numero // secondo_numero
    resto = primo_numero % secondo_numero

    print(f"Divisione normale: {divisione_normale} (tipo: {type(divisione_normale)})")
    print(f"Divisione intera: {divisione_intera} (tipo: {type(divisione_intera)})")
    print(f"Resto: {resto} (tipo: {type(resto)})")

# Esercizio 3: Manipolazione di Stringhe
def esercizio_3():
    print("\n=== Esercizio 3: Manipolazione di Stringhe ===")
    parola = input("Inserisci una parola: ")
    numero = int(input("Inserisci un intero: "))

    ripetizione = parola * numero
    lunghezza = len(parola)

    print(f"Ripetizione: {ripetizione} (tipo: {type(ripetizione)})")
    print(f"Lunghezza: {lunghezza} (tipo: {type(lunghezza)})")

# Esercizio 4: Conversione e Espressione Mista
def esercizio_4():
    print("\n=== Esercizio 4: Conversione e Espressione Mista ===")
    numero_stringa = input("Inserisci un numero: ")

    numero_intero = int(numero_stringa)
    numero_float = float(numero_stringa)

    risultato = numero_intero + numero_float * 2

    print(f"Risultato di {numero_intero} + {numero_float} * 2: {risultato} (tipo: {type(risultato)})")

# Esercizio 5: Valore Booleano di Oggetti
def esercizio_5():
    print("\n=== Esercizio 5: Valore Booleano di Oggetti ===")
    stringa = input("Inserisci una stringa: ")

    valore_booleano = bool(stringa)

    print(f"Valore booleano: {valore_booleano} (tipo: {type(valore_booleano)})")
    print("Nota: bool() restituisce False SOLO se la stringa è vuota")

# Funzione principale per eseguire tutti gli esercizi
def main():
    print("Esercizi per casa - Tipi di Dati, Input, Stampa, Conversioni ed Espressioni")
    print("=" * 70)

    esercizio_1()
    esercizio_2()
    esercizio_3()
    esercizio_4()
    esercizio_5()

if __name__ == "__main__":
    main()