ileBlokow=int(raw_input("W ilu blokach maja pojawic sie gwiazdki?: "))

for blok in range(1, ileBlokow +1):
    for linia in range(1, blok *2):
        for gwiazdka in range(1, (blok +linia)*2):
            print "*",
        print
    print
