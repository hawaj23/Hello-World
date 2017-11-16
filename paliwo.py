bak=float(raw_input("Jak du¿y jest bak w twoim samochodzie?: "))
paliwo=float(raw_input("Jaki jest obecny poziom paliwa w procentach?: "))
zasieg=float(raw_input("Ile kilometrów mo¿e przecjechaæ twój samochód na 1 litrze paliwa?: "))

kilometry = ((bak - 5) *(paliwo*0.01)*zasieg)

if kilometry <= 200:
    print "Rozmiar baku: ", bak, "\n" , "Poziom paliwa: ", paliwo, "\n", "Km na 1 litr: ", zasieg , "\n", "Mo¿esz przejechaæ jeszcze: ", kilometry, "km."
    print "Kolejna stacja jest za 200 km."
    print "Zatankuj teraz!"
else:
    print "Rozmiar baku: ", bak, "\n" , "Poziom paliwa: ", paliwo, "\n", "Km na 1 litr: ", zasieg , "\n", "Mo¿esz przejechaæ jeszcze: ", kilometry, "km."
    print "Kolejna stacja jest za 200 km."
    print "Mo¿esz zaczekaæ z tankowaniem do nastêpnej stacji!"


