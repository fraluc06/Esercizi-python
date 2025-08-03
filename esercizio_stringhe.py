# * prendere da utente nome, cognome ed età assicurandosi non ci siano spazi bianchi attorno
# * mandare a schermo una frase descrittiva della persona con le ultime 3 cifre del cognome in maiuscolo
# * assicurarsi che il nome sia con l'iniziale maiuscola e mandarne a schermo le prime 3 cifre
# ?età sommata alla lunghezza del cognome con 4 punti decimali
# ?mandare a schermo poi nome e cognome ed età separati da "-"
nome = input("Inserisci il tuo nome: ").strip()
cognome = input("Inserisci il tuo cognome: ").strip()
eta = input("Inserisci la tua età: ").strip()
print(cognome[-3:].upper())
print(nome.capitalize()[:3])
print(f"{int(eta) + len(cognome) :.4f}")
print(f"{nome}-{cognome}-{eta}")
