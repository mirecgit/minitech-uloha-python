import random

def vypocet_nakladov_na_prepravu(hmotnost, vzdialenost, typ_dopravy):

    match typ_dopravy:
        case 1: # nákladne auto
            officer = random.choice(["Ján Novák (vodič auta)", "Anna Milá (vodička auta)"])
            cena_za_km = 0.5
        case 2: # loď
            officer = "Mária Horváthová (kapitánka lode)"
            cena_za_km = 0.3
        case 3: # lietadlo
            officer = "Peter Kováč (pilot)"
            cena_za_km = 1.0
        case _:
            print("Neplatný typ dopravy!")
            return

    cena_dopravy = hmotnost * vzdialenost * cena_za_km

    print(f"Celková cena dopravy: {cena_dopravy} eur")
    print(f"Officier: {officer}")

    return cena_dopravy

