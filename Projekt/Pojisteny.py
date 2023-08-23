class Pojisteny:
    def __init__(self, jmeno, prijmeni, vek, telefon):
        self.jmeno = jmeno       # Uložení jména
        self.prijmeni = prijmeni # Uložení příjmení
        self.vek = vek           # Uložení věku
        self.telefon = telefon   # Uložení telefonu

    def __str__(self): # Formátování objektu jako řetězce
        return f"Jméno: {self.jmeno} {self.prijmeni}, Věk: {self.vek}, Telefon: {self.telefon}"