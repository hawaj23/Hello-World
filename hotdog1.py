print "\tParowka\tBulka\tKetchup\tMusztar\tCebula"
licznik = 1
for parowka in [0,1]:
    for bulka in [0,1]:
        for ketchup in [0,1]:
            for musztarda in [0,1]:
                for cebula in [0,1]:
                    print "#", licznik, "\t",
                    print parowka, "\t", bulka, "\t", ketchup, "\t",
                    print musztarda, "\t", cebula
                    licznik = licznik + 1
