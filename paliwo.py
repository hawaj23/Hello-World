bak=float(raw_input("Jak du�y jest bak w twoim samochodzie?: "))
paliwo=float(raw_input("Jaki jest obecny poziom paliwa w procentach?: "))
zasieg=float(raw_input("Ile kilometr�w mo�e przecjecha� tw�j samoch�d na 1 litrze paliwa?: "))

kilometry = ((bak - 5) *(paliwo*0.01)*zasieg)

if kilometry <= 200:
    print "Rozmiar baku: ", bak, "\n" , "Poziom paliwa: ", paliwo, "\n", "Km na 1 litr: ", zasieg , "\n", "Mo�esz przejecha� jeszcze: ", kilometry, "km."
    print "Kolejna stacja jest za 200 km."
    print "Zatankuj teraz!"
else:
    print "Rozmiar baku: ", bak, "\n" , "Poziom paliwa: ", paliwo, "\n", "Km na 1 litr: ", zasieg , "\n", "Mo�esz przejecha� jeszcze: ", kilometry, "km."
    print "Kolejna stacja jest za 200 km."
    print "Mo�esz zaczeka� z tankowaniem do nast�pnej stacji!"


