forme_geometriche = ["quadrato", "rettangolo", "triangolo", "cerchio"]


def calcola_area(forma: str, dimensioni:list[int])-> float:
    forma = forma.lower().strip()
    if forma == "quadrato":
        lato = dimensioni[0]
        return lato * lato
    elif forma == "rettangolo":
        base = dimensioni[0]
        altezza = dimensioni[1]
        return base * altezza
    elif forma == "triangolo":
        base = dimensioni[0]
        altezza = dimensioni[1]
        return (base * altezza) / 2
    elif forma == "cerchio":
        raggio = dimensioni[0]
        return 3.14 * raggio * raggio
    else:
        raise ValueError("Forma geometrica non valida. Scegli tra quadrato, rettangolo, triangolo o cerchio.")
print (calcola_area("quadrato", [5])) # Esempio di chiamata alla funzione