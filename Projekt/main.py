from Pojisteny import Pojisteny
from SpravaPojisteny import SpravaPojisteny

sprava_pojisteny = SpravaPojisteny() # Vytvoření instance

# Nadpis
print("=========================="
      " \n   Evidence Pojištěných "
      "\n==========================")

while True:
    print("\n1 - Přidat pojištěného")
    print("2 - Zobrazit všechny pojištěné")
    print("3 - Hledat pojištěného")
    print("4 - Konec")

    valid_choices = [1, 2, 3, 4]

    # error handler, kdy volba je jiná než 1 až 4
    try:
        volba = int(input("\nVyberte možnost: "))
        if volba not in valid_choices:
            raise ValueError
    except ValueError:
        print("\nNeplatná volba. Zadejte prosím číslo 1, 2, 3 nebo 4.\n")
        continue

    if volba == 1:
        while True:
            jmeno = input("Zadejte jméno: ")
            prijmeni = input("Zadejte příjmení: ")

            if jmeno and prijmeni:  # Zkontroluje zda není jméno nebo příjmení prázdné
                break
            else:
                print("\nJméno a příjmení nesmí být prázdné.\n")

    # error handler, kdy hodnota věku není kladné číslo
        while True:
            try:
                vek = int(input("Zadejte věk: "))
                assert vek >= 0
                break
            except (ValueError, AssertionError):
                print("Neplatný formát věku. Zadejte prosím správný formát.")

        telefon = input("Zadejte telefonní číslo: ")
        osoba = Pojisteny(jmeno, prijmeni, vek, telefon)
        sprava_pojisteny.pridat_pojisteneho(osoba)
        print("\nData byla uložena.\n")

    elif volba == 2:
        vsechny_osoby = sprava_pojisteny.vrat_vsechny_pojistene()
        for osoba in vsechny_osoby:
            print(osoba)      # Vytiskne informace o každé osobě

    elif volba == 3:
        hledane_jmeno = input("Zadejte jméno: ")
        hledane_prijmeni = input("Zadejte příjmení: ")
        nalezena_osoba = sprava_pojisteny.najit_pojisteneho(hledane_jmeno, hledane_prijmeni)
        if nalezena_osoba:
            print("\nNalezeno:")
            for osoba in nalezena_osoba:
                print(osoba)  # Samostatný řádek
        else:
            print("\nOsoba nenalezena (Zkontrolujte velká, malá písmena a mezery).\n")
    elif volba == 4:
        print("Ukončuji...")
        break
    else:
        print("\nNeplatná volba. Prosím vyberte znovu.\n")