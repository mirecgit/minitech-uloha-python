# Úloha 2.5
# Predpokladajme, že ak sa objedná viac ako 50 000 kg ryže, tak cena za kilogram sa zníži na 2 eurá z pôvodných 2.50 eur. Upravte program, aby toto zohľadnil.

import naklady


pocet_ludi = int(input("Zadajte počet ľudí v núdzi: "))
rozpocet = naklady.vypocet_nakladov_na_ryzu(pocet_ludi)

print(f"Nákup ryže bude stáť: {rozpocet} eur")

# Výstup:
#
# Zadajte počet ľudí v núdzi: 10000
# Objednane množstvo ryže: 30000 kg
# Cena ryže za kilogram: 2.5 eur
# Nákup ryže bude stáť: 75000.0 eur

# Zadajte počet ľudí v núdzi: 20000
# Objednane množstvo ryže: 60000 kg
# Cena ryže za kilogram: 2 eur
# Nákup ryže bude stáť: 120000 eur

# Zadajte počet ľudí v núdzi: 16666
# Objednane množstvo ryže: 49998 kg
# Cena ryže za kilogram: 2.5 eur
# Nákup ryže bude stáť: 124995.0 eur

# Zadajte počet ľudí v núdzi: 16667
# Objednane množstvo ryže: 50001 kg
# Cena ryže za kilogram: 2 eur
# Nákup ryže bude stáť: 100002 eur