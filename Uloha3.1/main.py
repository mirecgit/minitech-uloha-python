# Úloha 3.1
# Výpočet nákladov na dopravu a priradenie vodičov
# Vytvorte program, ktorý vypočíta celkové náklady na distribúciu potravín na základe hmotnosti potravín, vzdialenosti, a typu dopravy (nákladné auto, loď, lietadlo).
# Na základe typu dopravy priradí Officera ako vodiča pre daný spôsob prepravy.
# Tieto funkcie budú umiestnené v samostatnom súbore a budú volané z hlavného súboru.
# auto má cenu za km 0.50, loď má cenu 0.30, letadlo má cenu 1.00
# od užívateľa získame vstupy na hmotnosť, vzdialenosť a typ dpravy
# Officers sú Ján Novák (vodič auta), Mária Horváthová (kapitánka lode), Peter Kováč (pilot), Anna Milá (vodička auta

import naklady

hmotnost = int(input("Zadajte hmotnosť potravín (kg): "))
vzdialenost = int(input("Vzdialenost prepravy (km): "))
typ_dopravy = int(input("Zadajte typ dopravy (1 - nákladne auto, 2 - loď, 3 - lietadlo): "))

naklady.vypocet_nakladov_na_prepravu(hmotnost, vzdialenost, typ_dopravy)

# Výstup:
#
# Zadajte hmotnosť potravín (kg): 100
# Vzdialenost prepravy (km): 250
# Zadajte typ dopravy (1 - nákladne auto, 2 - loď, 3 - lietadlo): 1
# Celková cena dopravy: 12500.0 eur
# Officier: Ján Novák (vodič auta)
#
# Zadajte hmotnosť potravín (kg): 100
# Vzdialenost prepravy (km): 250
# Zadajte typ dopravy (1 - nákladne auto, 2 - loď, 3 - lietadlo): 1
# Celková cena dopravy: 12500.0 eur
# Officier: Anna Milá (vodička auta)
#
# Zadajte hmotnosť potravín (kg): 100
# Vzdialenost prepravy (km): 250
# Zadajte typ dopravy (1 - nákladne auto, 2 - loď, 3 - lietadlo): 2
# Celková cena dopravy: 7500.0 eur
# Officier: Mária Horváthová (kapitánka lode)
#
# Zadajte hmotnosť potravín (kg): 100
# Vzdialenost prepravy (km): 250
# Zadajte typ dopravy (1 - nákladne auto, 2 - loď, 3 - lietadlo): 3
# Celková cena dopravy: 25000.0 eur
# Officier: Peter Kováč (pilot)

# Zadajte hmotnosť potravín (kg): 100
# Vzdialenost prepravy (km): 250
# Zadajte typ dopravy (1 - nákladne auto, 2 - loď, 3 - lietadlo): 4
# Neplatný typ dopravy!