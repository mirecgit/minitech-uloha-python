# Úloha 2.4
# Upravte program tak, aby sa opýtal na počet ľudí, na cenu ryže za kilogram a potom vypočítal celkové náklady na ryžu.

import naklady


pocet_ludi = int(input("Zadajte počet ľudí v núdzi: "))
cena_ryze_kg = float(input("Zadajte cenu ryže za kilogram: "))

rozpocet = naklady.vypocet_nakladov_na_ryzu(pocet_ludi, cena_ryze_kg)

print(f"Nákup ryže bude stáť: {rozpocet} eur")

# Výstup:
#
# Zadajte počet ľudí v núdzi: 20000
# Zadajte cenu ryže za kilogram: 2.5
# Nákup ryže bude stáť: 150000.0 eur