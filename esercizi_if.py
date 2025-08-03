libreria = {
"Il Signore degli Anelli": {"autore": "J.R.R. Tolkien", "copie_disponibili": 5},
"Harry Potter": {"autore": "J.K. Rowling", "copie_disponibili": 3},
"1984": {"autore": "George Orwell", "copie_disponibili": 2},
"Il Codice Da Vinci": {"autore": "Dan Brown", "copie_disponibili": 0},
"Il Grande Gatsby": {"autore": "F. Scott Fitzgerald", "copie_disponibili": 4}
}


titolo_input = input("Inserisci il titolo del libro: ").strip().lower()

if titolo_input in libreria:
    autore = libreria[titolo_input]
    copie_disponibili = autore["copie_disponibili"]
    if copie_disponibili > 0:
        print(f"Il libro '{titolo_input}' di {autore['autore']} è disponibile. Copie disponibili: {copie_disponibili}.")
    else:
        print(f"Il libro '{titolo_input}' di {autore['autore']} non è disponibile al momento.")
        scelta = input("Vuoi essere avvisato quando sarà disponibile? (sì/no): ").strip().lower()
        if scelta == "sì":
            print(f"Ti avviseremo quando '{titolo_input}' sarà disponibile.")
            print("Grazie per la tua richiesta!")
        else:
            print(f"Il libro '{titolo_input}' non è presente nella nostra libreria. Non ti avviseremo quando sarà disponibile.")
            print("Grazie per aver visitato la nostra libreria!")