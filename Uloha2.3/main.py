# Úloha 2.3
# Upravte predchádzajúcu funkciu tak, aby sa program opýtal na počet ľudí v núdzi a užívateľ ho zadal, potom vypočítal náklady na ryžu.

import naklady


pocet_ludi = int(input("Zadajte počet ľudí v núdzi: "))
rozpocet = naklady.vypocet_nakladov_na_ryzu(pocet_ludi)

print(f"Nákup ryže bude stáť: {rozpocet} eur")

# Výstup:
#
# Zadajte počet ľudí v núdzi: 20000
# Nákup ryže bude stáť: 150000.0 eur