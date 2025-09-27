note_freq = [
    440.00,  # La
    493.88,  # Si
    261.63,  # Do
    293.66,  # Re
    329.63,  # Mi
    349.23,  # Fa
    392.00  # Sol
]
lettere_alfabeto = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G'
]

lettera_inserita = input("Inserisci una nota (A, B, C, D, E, F, G): ")


def get_note_freq(note: str) -> dict[str, float]:
    note = note.upper().strip()
    if note not in lettere_alfabeto:
        raise ValueError("Nota non valida. Inserisci una nota tra A, B, C, D, E, F, G.")
    return {letter: freq for letter, freq in zip(lettere_alfabeto, note_freq) if letter == note}


print(get_note_freq(lettera_inserita))