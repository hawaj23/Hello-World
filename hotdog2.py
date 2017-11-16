par_kal = 140
bulka_kal = 120
muszt_kal = 20
ket_kal = 80
ceb_kal = 40

print "\tParowka\tBulka\tKetchup\tMusztar\tCebula\tKalorie"
licznik = 1
for parowka in [0,1]:
    for bulka in [0,1]:
        for ketchup in [0,1]:
            for musztarda in [0,1]:
                for cebula in [0,1]:
                    razem_kal = (parowka*par_kal)+(bulka*bulka_kal)+(musztarda*muszt_kal)+(ketchup*ket_kal)+(cebula*ceb_kal)
                    print "#", licznik, "\t",
                    print parowka, "\t", bulka, "\t", ketchup, "\t",
                    print musztarda, "\t", cebula,
                    print "\t", razem_kal
                    licznik = licznik + 1
