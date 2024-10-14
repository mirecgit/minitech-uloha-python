def vypocet_nakladov_na_ryzu(pocet_ludi):    
    ryza_na_osobu = 3 # kg

    objednane_mnozstvo_ryze_kg = pocet_ludi * ryza_na_osobu
    
    if objednane_mnozstvo_ryze_kg > 50000:
        cena_ryze_kg = 2 # eur
    else:
        cena_ryze_kg = 2.5 # eur

    print(f"Objednane množstvo ryže: {objednane_mnozstvo_ryze_kg} kg")
    print(f"Cena ryže za kilogram: {cena_ryze_kg} eur")
    
    rozpocet = objednane_mnozstvo_ryze_kg * cena_ryze_kg
    return rozpocet