dlugosc = float(raw_input ("WprowadŸ d³ugoœæ pokoju: "))
szerokosc = float (raw_input ("WprowadŸ szerokoœæ pokoju: "))
cena = float (raw_input ("WprowadŸ cenê 1m2 wyk³adziny: "))
powierzchnia = dlugosc * szerokosc
koszt = cena * powierzchnia
centymetry = powierzchnia * 1000
print "Niezbêdna powierzchnia wyk³adziny w metrach to: " , powierzchnia, "m2"
print "Niezbêdna powierzchnia wyk³adziny w centymetrach to: " , centymetry, "cm2"
print "Ca³kowity koszt wyk³adziny  to: " , koszt, "PLN.",
