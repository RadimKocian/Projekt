class SpravaPojisteny:
    def __init__(self):
        self.pojisteni_lide = []

    # Přidání pojištěné osoby do seznamu
    def pridat_pojisteneho(self, osoba):
        self.pojisteni_lide.append(osoba)

    # Vrátí seznam všech pojištěných osob
    def vrat_vsechny_pojistene(self):
        return self.pojisteni_lide

    def najit_pojisteneho(self, jmeno, prijmeni):
        vysledek_hledani = []  # Prázdný seznam pro shodné osoby
        for osoba in self.pojisteni_lide:  # Procházení seznamu pojištěných osob
            if osoba.jmeno == jmeno and osoba.prijmeni == prijmeni:  # Kontrola jména a příjmení
                vysledek_hledani.append(str(osoba))  # Přidání shodné osoby do seznamu
        return vysledek_hledani  # Vrátí seznam shodných osob