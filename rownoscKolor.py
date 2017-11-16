wiek= float(raw_input("Wprowadz swoj wiek: "))
klasa=float(raw_input("Do ktorej klasy chodzisz? "))
kolor=raw_input("Jaki jest twoj ulubiony kolor?: ")
if wiek >= 8 and klasa >= 3 and kolor == "zielony":
    print "Mo¿esz rozpocz¹æ grê."
else:
    print "Niestety nie mo¿esz zagraæ w tê grê."
