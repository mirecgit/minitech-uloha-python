# Python workshop - praca na doma

## Úloha 2
### Úloha 2.1
Zjednodušme si svet: Vieme, že v jednej oblasti je 20 000 ľudí v núdzi, na každého z
nich sa musí zabezpečiť 3 kg ryže, kde 1 kg ryže stojí 2.50 eur. Koľko nás bude stáť len
nákup ryže?

### Úloha 2.2
Prehodenie do funkcie - v jednej oblasti je x ľudí v núdzi, objednávame 3 kg ryže na
osobu za 2.50 eur za kilogram. Počet ľudí nám musí niekto zadať, aby sme mohli
vypočítať celkové náklady. Definujte funkciu, ktorú zavoláte a vypočítate cenu nákupu
ryže.
`naklady.py`
```python
def vypocet_nakladov_na_ryzu(pocet_ludi):
ryza_na_osobu = 3 # kg
cena_ryze_kg = 2.50 # eur
rozpocet = pocet_ludi * ryza_na_osobu * cena_ryze_kg
return rozpocet
```
`main.py`

```python
import naklady
# Príklad použitia:
pocet_ludi = 20000
rozpocet = naklady.vypocet_nakladov_na_ryzu(pocet_ludi)
print(f"Nákup ryže bude stáť: {rozpocet} eur")
```

### Úloha 2.3
Upravte predchádzajúcu funkciu tak, aby sa program opýtal na počet ľudí v núdzi a
užívateľ ho zadal, potom vypočítal náklady na ryžu.

### Úloha 2.4
Upravte program tak, aby sa opýtal na počet ľudí, na cenu ryže za kilogram a potom
vypočítal celkové náklady na ryžu.

### Úloha 2.5
Predpokladajme, že ak sa objedná viac ako 50 000 kg ryže, tak cena za kilogram sa
zníži na 2 eurá z pôvodných 2.50 eur. Upravte program, aby toto zohľadnil.

### Úloha 2.6
Okrem nákladov na ryžu ešte musíme započítať náklady na prepravu. Na každý
kilometer prepravy ryže sa účtuje 0.50 eur za kilogram. Predpokladajme, že ryža musí
byť prepravená na vzdialenosť 100 km. Vypočítajte celkové náklady na prepravu.

### Úloha 2.7

Ak je preprava do vzdialenejších oblastí (nad 200 km), tak sú náklady na prepravu
vyššie o 20%. Upravte predchádzajúci program, aby zohľadnil tento nárast nákladov pri
preprave na väčšie vzdialenosti.

## ULOHA 3
### ULOHA 3.1: Výpočet nákladov na dopravu a priradenie vodičov
Vytvorte program, ktorý vypočíta celkové náklady na distribúciu potravín na základe
hmotnosti potravín, vzdialenosti, a typu dopravy (nákladné auto, loď, lietadlo).
Na základe typu dopravy priradí Officera ako vodiča pre daný spôsob prepravy.
Tieto funkcie budú umiestnené v samostatnom súbore a budú volané z hlavného
súboru.
auto má cenu za km 0.50, loď má cenu 0.30, letadlo má cenu 1.00
od užívateľa získame vstupy na hmotnosť, vzdialenosť a typ dpravy
Officers sú Ján Novák (vodič auta), Mária Horváthová (kapitánka lode), Peter Kováč
(pilot), Anna Milá (vodička auta)