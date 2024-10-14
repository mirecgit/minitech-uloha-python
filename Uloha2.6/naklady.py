def vypocet_nakladov_na_ryzu(pocet_ludi):
    ryza_na_osobu = 3 # kg

    objednane_mnozstvo_ryze_kg = pocet_ludi * ryza_na_osobu

    if objednane_mnozstvo_ryze_kg > 50000:
        cena_ryze_kg = 2 # eur
    else:
        cena_ryze_kg = 2.5 # eur

    print(f"Objednane množstvo ryže: {objednane_mnozstvo_ryze_kg} kg")
    print(f"Cena ryže za kilogram: {cena_ryze_kg} eur")

    rozpocet = (objednane_mnozstvo_ryze_kg * cena_ryze_kg) + vypocet_nakladov_na_prepravu(objednane_mnozstvo_ryze_kg)
    return rozpocet

def vypocet_nakladov_na_prepravu(objednane_mnozstvo_ryze_kg):
    vzdialenost = 100 # km
    doprava_km = 0.50 # za kg
    celkove_naklady_na_prepravu = vzdialenost * doprava_km * objednane_mnozstvo_ryze_kg
    print(f"Celkové náklady na prepravu: {celkove_naklady_na_prepravu} eur (Vzdialenost: {vzdialenost}, doprava za km {doprava_km} eur)")
    return celkove_naklady_na_prepravu
