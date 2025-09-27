# Chiediamo il numero di studenti da inserire
# Chiediamo all'utente di inserire il nome degli studenti e i loro voti.
# Memorizziamo queste informazioni utilizzando una lista di dizionari,
# dove ogni dizionario contiene il nome e il voto di uno studente.
# Stampiamo i dettagli degli studenti e i loro voti.
num_studenti = int(input("Quanti studenti vuoi inserire? "))
studenti = []
for i in range(num_studenti):
    nome = input(f"Inserisci il nome dello studente {i + 1}: ")
    voto = float(input(f"Inserisci il voto di {nome}: "))
    studenti.append({"nome": nome, "voto": voto})
print("\nDettagli degli studenti:")
for studente in studenti:
    print(f"Nome: {studente['nome']}, Voto: {studente['voto']:.1f}")
    print(type(studente['nome']), type(studente['voto']))