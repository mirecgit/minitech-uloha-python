# Úloha 2.2
# Prehodenie do funkcie - v jednej oblasti je x ľudí v núdzi, objednávame 3 kg ryže na osobu za 2.50 eur za kilogram. 
# Počet ľudí nám musí niekto zadať, aby sme mohli vypočítať celkové náklady. Definujte funkciu, ktorú zavoláte a vypočítate cenu nákupu ryže.

import naklady

pocet_ludi = 20000
rozpocet = naklady.vypocet_nakladov_na_ryzu(pocet_ludi)
print(f"Nákup ryže bude stáť: {rozpocet} eur")

# Výstup:
#
# Nákup ryže bude stáť: 150000.0 eur