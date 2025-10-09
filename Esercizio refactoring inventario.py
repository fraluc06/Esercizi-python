# ESERCIZIO: REFACTORING DELL'INVENTARIO

# Inventario iniziale (formato lista)
inventario = [
    'Spada Leggendaria',
    'Pozione HP',
    'Pozione HP',
    'Pozione HP',
    'Scudo Magico'
]

print("=== TASK 1: Conversione da lista a dizionario ===")
# Esempio risultato: {'Spada Leggendaria': 1, 'Pozione HP': 3, 'Scudo Magico': 1}

inventario_dict = {item: inventario.count(item) for item in set(inventario)}

print("\n=== TASK 2: Visualizzazione inventario ===")

for item, quantita in inventario_dict.items():
    print(f"{item}: {quantita}")

print("\n=== TASK 3: Consumo pozione ===")
# - Un assegnamento potenziato (es. +=, -=)
# - Un if per rimuovere l'item se la quantità scende a 0

def consuma_pozione(inventario, nome_pozione):
    """
    Consuma una pozione dall'inventario.
    Se la quantità scende a 0, rimuove l'item.
    """
    if nome_pozione in inventario:
        inventario[nome_pozione] -= 1
        print(f"Hai consumato una {nome_pozione}.")

        if inventario[nome_pozione] <= 0:
            del inventario[nome_pozione]
            print(f"Hai esaurito tutte le {nome_pozione}. Rimosso dall'inventario.")
    else:
        print(f"Non hai nessuna {nome_pozione} nell'inventario.")

# Test della funzione
consuma_pozione(inventario_dict, 'Pozione HP')
print("\nInventario dopo consumo:")
for item, quantita in inventario_dict.items():
    print(f"{item}: {quantita}")
