# Esercizio 1
frutta = ["mela", "banana", "arancia"]
count = 0
for elemento in frutta:
    count += 1
    print(f"{elemento} è l'elemento numero {count}")
for frutto in ("fragola", "kiwi"):
    frutta.append(frutto)
print(frutta)

# Esercizio 2
voti ={}
fine = False
while not fine:
    nome = input("Inserisci il nome dello studente (o 'fine' per terminare): ").strip()
    if not nome:
        print("Nome non valido, riprova.")
        continue
    if nome.lower() == 'fine'.lower():
        fine = True
        break
    else:
        while True:
            voto = int(input(f"Inserisci il voto per {nome} (1-10): "))
            if voto in range(1, 11):
                voti[nome] = voto
                print(f"✓ Voto salvato!\n")
                break
            else:
                print("Voto non valido, deve essere tra 0 e 10.")
# # Stampa i risultati
print("\n" + "="*40)
print("RISULTATI FINALI")
print("="*40)

if len(voti) == 0:
    print("Nessuno studente inserito.")
else:
    promossi = sum(1 for v in voti.values() if v >= 6)

    print(f"\nStudenti con voto ≥ 6: {promossi} su {len(voti)}")

    print("\n--- TABELLA VOTI ---")
    print(f"{'Nome':<20} {'Voto':>5}")
    print("-" * 27)

    for nome, voto in voti.items():
        stato = "✓" if voto >= 6 else "✗"
        print(f"{nome:<20} {voto:>5} {stato}")

# Esercizio 5
import random
segreto = random.randint(1, 20)
for tentativo in range(1,6):
    numero = int(input(f"Inserisci un numero tentavivo:{tentativo}/5 "))
    if numero == segreto:
        print("Hai indovinato!")
        break
    elif numero < segreto:
        print("Il numero segreto è più grande.")
    else:
        print("Il numero segreto è più piccolo.")
else:
    print(f"Mi dispiace, il numero segreto era {segreto}.")