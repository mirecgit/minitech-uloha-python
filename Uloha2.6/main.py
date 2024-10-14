# Úloha 2.6
# Okrem nákladov na ryžu ešte musíme započítať náklady na prepravu. Na každý kilometer prepravy ryže sa účtuje 0.50 eur za kilogram. Predpokladajme, že ryža musí
# byť prepravená na vzdialenosť 100 km. Vypočítajte celkové náklady na prepravu.

import naklady


pocet_ludi = int(input("Zadajte počet ľudí v núdzi: "))
rozpocet = naklady.vypocet_nakladov_na_ryzu(pocet_ludi)

print(f"Nákup ryže bude stáť: {rozpocet} eur")

# Výstup:
#
# Zadajte počet ľudí v núdzi: 20000
# Objednane množstvo ryže: 60000 kg
# Cena ryže za kilogram: 2 eur
# Celkové náklady na prepravu: 3000000.0 eur (Vzdialenost: 100, doprava za km 0.5 eur)
# Nákup ryže bude stáť: 3120000.0 eur