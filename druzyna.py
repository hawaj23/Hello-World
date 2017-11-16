plec = raw_input("Wprowadz swoja plec w formacie d lub c: ")
if plec == "d":
    wiek = int(raw_input(" Wprowadz swoj wiek: "))
    if wiek >= 10 and wiek <= 12:
        print "Gratulacje zostalas przyjeta do druzyny!"
    else:
        print "Niestety nie masz odpowiedniego wieku!"
else:
    print "Niestety nie jesteœ dziewczyn¹!"
