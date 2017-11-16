# -*- coding: cp1250 -*-
grosz50 = int(raw_input("Proszę wprowadzić liczbę 50 groszówek: "))
grosz20 = int(raw_input("Proszę wprowadzić liczbę 20 groszówek: "))
grosz10 = int(raw_input("Proszę wprowadzić liczbę 10 groszówek: "))
grosz5 = int(raw_input("Proszę wprowadzić liczbę 5 groszówek: "))
suma = 0.5 * grosz50 + 0.2 * grosz20 + 0.1 * grosz10 + 0.05 * grosz5
print "Twoje oszczędności wynoszą: ", suma , "PLN"
