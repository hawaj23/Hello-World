dlugosc = float(raw_input ("Wprowad� d�ugo�� pokoju: "))
szerokosc = float (raw_input ("Wprowad� szeroko�� pokoju: "))
cena = float (raw_input ("Wprowad� cen� 1m2 wyk�adziny: "))
powierzchnia = dlugosc * szerokosc
koszt = cena * powierzchnia
centymetry = powierzchnia * 1000
print "Niezb�dna powierzchnia wyk�adziny w metrach to: " , powierzchnia, "m2"
print "Niezb�dna powierzchnia wyk�adziny w centymetrach to: " , centymetry, "cm2"
print "Ca�kowity koszt wyk�adziny  to: " , koszt, "PLN.",
