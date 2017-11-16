ileBlokow=int(raw_input("W ilu blokach maja pojawic sie gwiazdki?: "))
ileLinii=int(raw_input("W ilu liniach maja pojawic sie gwiazdki?: "))
ileGwiazdek=int(raw_input("Ile gwiazdek w linii?: "))

for blok in range(0, ileBlokow):
    for linia in range(0, ileLinii):
        for gwiazdka in range(0,ileGwiazdek):
            print "*",
        print
    print
