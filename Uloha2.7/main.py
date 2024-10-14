# Úloha 2.7
# Ak je preprava do vzdialenejších oblastí (nad 200 km), tak sú náklady na prepravu vyššie o 20%.
# Upravte predchádzajúci program, aby zohľadnil tento nárast nákladov pri preprave na väčšie vzdialenosti.

import naklady


pocet_ludi = int(input("Zadajte počet ľudí v núdzi: "))
vzdialenost = int(input("Vzdialenost prepravy (km): "))

rozpocet = naklady.vypocet_nakladov_na_ryzu(pocet_ludi, vzdialenost)

print(f"Nákup ryže bude stáť: {rozpocet} eur")

# Výstup:

# Zadajte počet ľudí v núdzi: 10000
# Vzdialenost prepravy (km): 100
# Objednane množstvo ryže: 30000 kg
# Cena ryže za kilogram: 2.5 eur
# Celkové náklady na prepravu: 1500000.0 eur (Vzdialenost: 100, doprava za km 0.5 eur)
# Nákup ryže bude stáť: 1575000.0 eur

# Zadajte počet ľudí v núdzi: 10000
# Vzdialenost prepravy (km): 205
# Objednane množstvo ryže: 30000 kg
# Cena ryže za kilogram: 2.5 eur
# Celkové náklady na prepravu su o 20% vyššie
# Celkové náklady na prepravu: 3690000.0 eur (Vzdialenost: 205, doprava za km 0.5 eur)
# Nákup ryže bude stáť: 3765000.0 eur